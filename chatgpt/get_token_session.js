// ==UserScript==
// @name         获取ChatGPT AccessToken/SessionToken
// @namespace    http://tampermonkey.net/
// @version      2.4
// @description  一键获取并复制OpenAI聊天的AccessToken或SessionToken，简化用户操作。
// @author       Flyrr & Yongmo & GPT-4
// @match        https://chat.openai.com/*
// @match        https://chatgpt.com/*
// @grant        GM_xmlhttpRequest
// @grant        GM_setClipboard
// @grant        GM_addStyle
// ==/UserScript==

(function() {
    'use strict';

    // 创建一个悬浮面板
    const panel = document.createElement('div');
    panel.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 1000; padding: 15px; border: 1px solid #ccc; border-radius: 12px; background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.3); font-family: "Microsoft YaHei", sans-serif; display: none; flex-direction: column; align-items: start;';
    // 创建展开面板按钮
    const toggleButton = document.createElement('button');
    toggleButton.textContent = '☰';
    toggleButton.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 1100; padding: 4px 8px; background: #007bff; color: white; cursor: pointer; font-size: 24px; border-radius: 6px; display: block;';


    // 添加通用按钮样式
    const buttonStyle = 'margin-bottom: 10px; padding: 8px 15px; border: none; border-radius: 6px; color: white; cursor: pointer; font-size: 16px; width: 100%; text-align: center;';

    // 创建Token类型选择器
    const tokenTypeSelector = document.createElement('select');
    tokenTypeSelector.style.cssText = 'width: 100%; margin-bottom: 10px; padding: 8px 10px; border-radius: 6px; border: 1px solid #ccc;';
    tokenTypeSelector.add(new Option('Access Token', 'access'), undefined);
    tokenTypeSelector.add(new Option('Session Token', 'session'), undefined);

    // 创建操作按钮
    const btnFetchAndCopy = document.createElement('button');
    btnFetchAndCopy.textContent = '获取并复制Token';
    btnFetchAndCopy.style.cssText = buttonStyle + 'background-color: #007bff;';

    // 创建文本显示区域
    const tokenDisplay = document.createElement('textarea');
    tokenDisplay.style.cssText = 'width: 100%; height: 60px; margin-bottom: 10px; padding: 10px; border-radius: 6px; border: 1px solid #ccc;';

    // 隐藏面板按钮
    const btnHidePanel = document.createElement('button');
    btnHidePanel.textContent = '隐藏面板';
    btnHidePanel.style.cssText = buttonStyle + 'background-color: #ffc107;';
    btnHidePanel.onclick = function() {
        panel.style.display = 'none';
        toggleButton.style.display = 'block';
    };

    // 将元素添加到面板
    panel.appendChild(tokenDisplay);
    panel.appendChild(tokenTypeSelector);
    panel.appendChild(btnFetchAndCopy);
    panel.appendChild(btnHidePanel);
    document.body.appendChild(panel);
    document.body.appendChild(toggleButton);

    // Toggle panel display
    toggleButton.onclick = function() {
        if (panel.style.display === 'none') {
            panel.style.display = 'flex';  // Show the panel
            toggleButton.style.display = 'none';  // Hide the toggle button
        } else {
            panel.style.display = 'none';  // Hide the panel
            toggleButton.style.display = 'block';  // Show the toggle button
        }
    };

    // 按钮点击事件：获取并复制Token
    btnFetchAndCopy.onclick = function() {
        if (tokenTypeSelector.value === 'access') {
            GM_xmlhttpRequest({
                method: "GET",
                url: "https://chat.openai.com/api/auth/session",
                onload: function(response) {
                    if (response.status >= 200 && response.status < 300) {
                        try {
                            const data = JSON.parse(response.responseText);
                            const accessToken = data.accessToken;
                            tokenDisplay.value = accessToken;
                            GM_setClipboard(accessToken, 'text');
                            alert('Access Token 已复制到剪贴板:\n' + accessToken);
                        } catch (e) {
                            console.error('解析返回数据错误:', e);
                            alert('解析返回数据错误，请查看控制台获取详细信息。');
                        }
                    } else {
                        console.error('获取AccessToken失败:', response.statusText);
                        alert('获取AccessToken失败: ' + response.statusText);
                    }
                }
            });
        } else if (tokenTypeSelector.value === 'session') {
            GM_xmlhttpRequest({
                method: "GET",
                url: "https://chat.openai.com/chat",
                onload: function(response) {
                    const cookieHeader = response.responseHeaders;
                    console.log("Headers:", cookieHeader);
                    const match = cookieHeader.match(/__Secure-next-auth.session-token=([^;]+);/);
                    if (match && match[1]) {
                        const sessionToken = match[1];
                        tokenDisplay.value = sessionToken;
                        GM_setClipboard(sessionToken, 'text');
                        //alert('Session Token 已复制到剪贴板:\n' + sessionToken);
                    } else {
                        alert('Session Token 未找到。可能是因为浏览器安全策略限制了头部信息的获取。');
                    }
                },
                onerror: function() {
                    alert('Failed to fetch session information.');
                }
            });
        }
    };
})();