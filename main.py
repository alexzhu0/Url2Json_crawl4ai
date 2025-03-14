import asyncio
import requests
import json
from crawl4ai import AsyncWebCrawler
import os
import sys
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

class DeepSeekClient:
    """用于与DeepSeek API交互的客户端"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DeepSeek API密钥未提供，请设置DEEPSEEK_API_KEY环境变量或直接传入API密钥")
        
        self.base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        self.api_url = f"{self.base_url}/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def analyze_content(self, content: str) -> Dict[str, Any]:
        """使用DeepSeek API分析文章内容"""
        
        prompt = f"""
请对以下文章内容进行分析，提取以下信息：
1. 文章标题
2. 作者信息
3. 发布日期
4. 来源网站
5. 主要话题和关键词（最多5个）
6. 文章摘要（200字以内）

请以JSON格式返回，包含以上字段。

文章内容：
{content}
"""
        
        payload = {
            "model": "deepseek-reasoner",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 8000
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()
            
            # 从DeepSeek响应中提取内容
            content = result["choices"][0]["message"]["content"]
            
            # 尝试将内容解析为JSON
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # 如果不是有效JSON，则返回原始文本
                return {"raw_analysis": content}
            
        except Exception as e:
            print(f"调用DeepSeek API时出错: {str(e)}")
            return {"error": str(e)}

async def crawl_and_analyze(url: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """爬取网页并使用DeepSeek分析内容"""
    
    # 创建爬虫实例并爬取内容
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        content = result.markdown
    
    # 使用DeepSeek API分析内容
    client = DeepSeekClient(api_key)
    analysis = client.analyze_content(content)
    
    # 组合原始内容和分析结果
    return {
        "url": url,
        "raw_content": content,
        "analysis": analysis
    }

def print_analysis_result(result: Dict[str, Any]) -> None:
    """格式化打印分析结果"""
    print("\n" + "="*80)
    print("网页内容分析结果")
    print("="*80)
    
    analysis = result.get("analysis", {})
    
    print(f"网址: {result['url']}")
    
    if "error" in analysis:
        print(f"\n分析出错: {analysis['error']}")
        return
    
    if "raw_analysis" in analysis:
        print("\n分析结果:")
        print(analysis["raw_analysis"])
    else:
        print(f"\n标题: {analysis.get('文章标题', '未提取')}")
        print(f"作者: {analysis.get('作者信息', '未提取')}")
        print(f"日期: {analysis.get('发布日期', '未提取')}")
        print(f"来源: {analysis.get('来源网站', '未提取')}")
        
        if "主要话题和关键词" in analysis:
            print(f"关键词: {analysis['主要话题和关键词']}")
        
        if "文章摘要" in analysis:
            print("\n摘要:")
            print(analysis["文章摘要"])
    
    print("\n" + "="*80)
    print("原始爬取内容")
    print("="*80)
    
    # 确保原始内容被完整打印
    raw_content = result.get("raw_content", "未获取到内容")
    print(raw_content)
    
    print("="*80)

def check_dependencies():
    """检查并提示安装必要的依赖"""
    try:
        # 尝试导入playwright
        import playwright
        return True
    except ImportError:
        print("\n缺少必要的依赖: playwright")
        print("请运行以下命令安装:")
        print("pip install playwright")
        print("playwright install")
        return False
    except Exception as e:
        print(f"\n检查依赖时出错: {str(e)}")
        return False

async def main():
    """主函数：处理用户输入并执行爬取分析流程"""
    
    print("网页内容爬取与分析工具")
    print("-"*30)
    
    # 检查依赖
    if not check_dependencies():
        print("\n请安装必要的依赖后重新运行程序。")
        return
    
    # 获取DeepSeek API密钥
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        api_key = input("请输入您的DeepSeek API密钥: ")
        os.environ["DEEPSEEK_API_KEY"] = api_key
    
    while True:
        # 获取用户输入的URL
        url = input("\n请输入要爬取的网址 (输入'q'退出): ")
        
        if url.lower() == 'q':
            break
        
        try:
            # 爬取并分析内容
            print(f"\n正在爬取和分析: {url}")
            result = await crawl_and_analyze(url, api_key)
            
            # 清理控制台输出，避免混乱
            print("\n\n")
            
            # 打印分析结果
            print_analysis_result(result)
            
        except Exception as e:
            print(f"\n处理过程中出错: {str(e)}")
            if "Executable doesn't exist" in str(e) or "playwright" in str(e).lower():
                print("\n看起来Playwright浏览器组件未安装。")
                print("请运行以下命令安装Playwright浏览器:")
                print("playwright install")
    
    print("\n感谢使用，再见！")

# 程序入口点
if __name__ == "__main__":
    asyncio.run(main())