# Integrate with Third-Party Authentication

<!--not needed anymore-->

ECP offers two methods for authenticating user login: basic authentication and integration with third-party authentication using the SAML protocol.

## What is the SAML Protocol?

SAML (Security Assertion Markup Language) is an XML-based open standard protocol used for exchanging authentication and authorization data in cross-network communications. SAML aims to facilitate secure communication and enable Single Sign-On (SSO) for user authentication across various network resources. 

## Configure SSO

Log in as system administrator. Click **System Settings** -> **General Settings**. 使用**系统管理员**在系统管理界面的**系统设置**-**通用配置**中设置**单点登录**。

1. 点击**添加 SAML 服务**，弹出配置对话框；
2. 添加 SSO 的**名称**；
3. **启用** SAML 服务；
4. 填写**登录 URL**，即第三方认证的登录地址；
5. 填写**登出 URL**，即第三方认证的登出地址；
6. 可以开启**签名请求**，如果开启，ECP 会自动生成一个签名；
7. 可以开启**强制登录**，如果开启，通过第三方登录时每次都需要输入用户名密码；
8. 可以开启**校验签名**，如果开启，请上传从第三方认证系统导出的公钥文件，并以 Base64 加密后上传；
9. 点击**确认**，以上配置生效。


<img src="./_assets/saml.png" style="zoom:100%;" align="middle">
