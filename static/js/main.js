document.addEventListener('DOMContentLoaded', function() {
    // 获取DOM元素
    const urlInput = document.getElementById('url-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const loadingElement = document.getElementById('loading');
    const resultContainer = document.getElementById('result-container');
    const errorContainer = document.getElementById('error-container');
    const errorText = document.getElementById('error-text');
    
    // 分析结果元素
    const articleTitle = document.getElementById('article-title');
    const authorElement = document.getElementById('author');
    const dateElement = document.getElementById('date');
    const sourceElement = document.getElementById('source');
    const urlElement = document.getElementById('url');
    const keywordsContainer = document.getElementById('keywords-container');
    const summaryText = document.getElementById('summary-text');
    const rawContentText = document.getElementById('raw-content-text');
    const formattedJsonElement = document.getElementById('formatted-json');
    
    // 标签切换
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');
            
            // 更新按钮状态
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // 更新内容显示
            tabContents.forEach(content => {
                if (content.id === tabName) {
                    content.classList.add('active');
                } else {
                    content.classList.remove('active');
                }
            });
        });
    });
    
    // 分析按钮点击事件
    analyzeBtn.addEventListener('click', () => {
        const url = urlInput.value.trim();
        
        if (!url) {
            showError('请输入要分析的网址');
            return;
        }
        
        // 显示加载状态
        loadingElement.classList.remove('hidden');
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
        
        // 发送请求到后端
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        })
        .then(response => response.json())
        .then(data => {
            // 隐藏加载状态
            loadingElement.classList.add('hidden');
            
            if (data.error) {
                showError(data.error);
                return;
            }
            
            // 显示结果
            displayResults(data);
            resultContainer.classList.remove('hidden');
        })
        .catch(error => {
            loadingElement.classList.add('hidden');
            showError('请求失败: ' + error.message);
        });
    });
    
    // 显示错误信息
    function showError(message) {
        errorText.textContent = message;
        errorContainer.classList.remove('hidden');
        resultContainer.classList.add('hidden');
    }
    
    // 显示分析结果
    function displayResults(data) {
        const analysis = data.analysis || {};
        
        // 更新URL
        urlElement.textContent = data.url;
        
        // 更新分析结果
        if (analysis.error) {
            showError('分析出错: ' + analysis.error);
            return;
        }
        
        // 更新标题
        if (analysis['文章标题']) {
            articleTitle.textContent = analysis['文章标题'];
        } else if (analysis.raw_analysis) {
            articleTitle.textContent = '分析结果';
        } else {
            articleTitle.textContent = '未提取到标题';
        }
        
        // 格式化JSON显示
        if (analysis.raw_analysis) {
            // 如果返回的是原始文本而非JSON
            formattedJsonElement.textContent = analysis.raw_analysis;
        } else {
            // 格式化JSON并添加换行
            let formattedJson = '{\n';
            
            if (analysis['文章标题']) {
                formattedJson += '  "文章标题": "' + analysis['文章标题'] + '",\n';
            }
            
            if (analysis['作者信息']) {
                formattedJson += '  "作者信息": "' + analysis['作者信息'] + '",\n';
            }
            
            if (analysis['发布日期']) {
                formattedJson += '  "发布日期": "' + analysis['发布日期'] + '",\n';
            }
            
            if (analysis['来源网站']) {
                formattedJson += '  "来源网站": "' + analysis['来源网站'] + '",\n';
            }
            
            if (analysis['主要话题和关键词']) {
                let keywords = analysis['主要话题和关键词'];
                if (typeof keywords === 'string') {
                    keywords = keywords.split(/[,，、]/);
                }
                
                formattedJson += '  "主要话题和关键词": [\n';
                keywords.forEach((keyword, index) => {
                    if (keyword && keyword.trim()) {
                        formattedJson += '    "' + keyword.trim() + '"';
                        if (index < keywords.length - 1) {
                            formattedJson += ',';
                        }
                        formattedJson += '\n';
                    }
                });
                formattedJson += '  ],\n';
            }
            
            if (analysis['文章摘要']) {
                formattedJson += '  "文章摘要": "' + analysis['文章摘要'] + '"\n';
            }
            
            formattedJson += '}';
            
            formattedJsonElement.textContent = formattedJson;
        }
        
        // 更新原始内容
        rawContentText.textContent = data.raw_content || '未获取到原始内容';
    }
    
    // 按下回车键触发分析
    urlInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            analyzeBtn.click();
        }
    });
});