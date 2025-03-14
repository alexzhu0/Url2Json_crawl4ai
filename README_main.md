# 网页内容爬取与分析工具

这是一个基于Python的网页内容爬取与分析工具，使用crawl4ai库爬取网页内容，并通过DeepSeek API进行智能分析，提取文章的关键信息。

## 功能特点

- 爬取指定网页的内容
- 使用DeepSeek API分析文章内容
- 提取文章标题、作者、发布日期、来源网站等信息
- 生成文章关键词和摘要
- 显示原始爬取内容，方便对比分析结果

## 环境要求

- Python 3.6+
- WSL或Linux环境（推荐）
- Conda环境管理

## 依赖库

- crawl4ai
- requests
- python-dotenv
- playwright（用于网页渲染）

## 安装步骤

1. 克隆或下载本项目到本地
2. 创建并激活conda环境
   ```
   conda create -n crawl4ai python=3.9
   conda activate crawl4ai
   ```
3. 安装所需依赖
   ```
   pip install python-dotenv requests crawl4ai playwright
   playwright install
   ```
4. 配置DeepSeek API密钥
   - 在项目根目录创建`.env`文件
   - 添加以下内容（替换为您的API密钥）
     ```
     DEEPSEEK_API_KEY="your_api_key_here"
     DEEPSEEK_BASE_URL="https://api.deepseek.com"
     ```

## 使用方法

1. 激活conda环境
   ```
   conda activate crawl4ai
   ```
2. 运行程序
   ```
   python main.py
   ```
3. 根据提示输入要爬取的网址
4. 查看分析结果和原始内容
5. 输入'q'退出程序

## 示例输出

程序会输出两部分内容：

1. **网页内容分析结果**：包括标题、作者、日期、来源、关键词和摘要
2. **原始爬取内容**：网页的原始内容

## 注意事项

- 确保已安装Playwright浏览器组件
- 需要有效的DeepSeek API密钥
- 部分网站可能有反爬虫措施，影响爬取效果

## 未来改进方向

- 添加批量处理URL的功能
- 支持将结果保存到文件
- 增加更多自定义分析选项
- 优化爬取性能和稳定性

## 许可证

MIT
