// ==UserScript==
// @name         OpenAI Token增强型管理
// @namespace    http://tampermonkey.net/
// @version      2.4
// @description  通过一键操作直接从用户界面获取、复制Access Token，提升您的OpenAI聊天体验。
// @author       Yongmo & GPT-4
// @match        https://chat.openai.com/*
// @match        https://chatgpt.com/*
// @grant        GM_xmlhttpRequest
// @grant        GM_setClipboard
// @grant        GM_addStyle
// @downloadURL https://update.greasyfork.org/scripts/492978/OpenAI%20Token%E5%A2%9E%E5%BC%BA%E5%9E%8B%E7%AE%A1%E7%90%86.user.js
// @updateURL https://update.greasyfork.org/scripts/492978/OpenAI%20Token%E5%A2%9E%E5%BC%BA%E5%9E%8B%E7%AE%A1%E7%90%86.meta.js
// ==/UserScript==

(function() {
    'use strict';

    // 创建一个悬浮面板，用于放置按钮和显示Token信息
    const panel = document.createElement('div');
    panel.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 1000; padding: 15px; border: 1px solid #ccc; border-radius: 12px; background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.3); font-family: "Microsoft YaHei", sans-serif; display: flex; flex-direction: column; align-items: start;';

    // 添加按钮样式
    const buttonStyle = 'margin-bottom: 10px; padding: 8px 15px; border: none; border-radius: 6px; color: white; cursor: pointer; font-size: 16px; width: 100%; text-align: center;';

    // 获取AccessToken按钮
    const btnFetchToken = document.createElement('button');
    btnFetchToken.textContent = '获取 AccessToken';
    btnFetchToken.style.cssText = buttonStyle + 'background-color: #28a745;';

    // 显示AccessToken的文本区域
    const accessTokenDisplay = document.createElement('textarea');
    accessTokenDisplay.style.cssText = 'width: 100%; height: 60px; margin-bottom: 10px; padding: 10px; border-radius: 6px; border: 1px solid #ccc;';

    // 一键复制AccessToken按钮
    const btnCopyAccessToken = document.createElement('button');
    btnCopyAccessToken.textContent = '复制 AccessToken';
    btnCopyAccessToken.style.cssText = buttonStyle + 'background-color: #007bff;';


    // 将按钮和显示区域添加到面板
    panel.appendChild(btnFetchToken);
    panel.appendChild(accessTokenDisplay);
    panel.appendChild(btnCopyAccessToken);
    document.body.appendChild(panel);

    function getToken() {
        fetch("https://chatgpt.com/api/auth/session", {
            method: "GET",
            headers: {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                'User-Agent': navigator.userAgent,
                'Origin': 'https://chatgpt.com',
                'Referer': 'https://chatgpt.com/',
                'Sec-Ch-Ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                'Sec-Ch-Ua-Arch': '"x86"',
                'Sec-Ch-Ua-Bitness': '"64"',
                'Sec-Ch-Ua-Full-Version': '"117.0.2045.7"',
                'Sec-Ch-Ua-Full-Version-List': '"Microsoft Edge";v="117.0.2045.7", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.11"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Model': '""',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // 获取accessToken
            const accessToken = data.accessToken;
            if (accessToken) {
                accessTokenDisplay.value = accessToken;
                console.log(`Access Token: ${accessToken}`);
            } else {
                console.error('Access Token not found in the response.');
            }
        })
        .catch(error => {
            console.error('Request failed:', error);
        });
    };

    // 按钮点击事件：获取AccessToken
    btnFetchToken.onclick = function() {
        return getToken();
    };

    // 按钮点击事件：复制AccessToken
    btnCopyAccessToken.onclick = function() {
        var accessToken = accessTokenDisplay.value;
        if (!accessToken) {
            getToken();
            accessToken = accessTokenDisplay.value;
        }
        const message = '' + accessToken;
        GM_setClipboard(message, 'text');
        //alert('已复制到剪贴板:\n' + message);
    };
})();
