# Development Requirements

Use this file as the single place to record cross-cutting implementation requirements before feature development starts.

## Design references

- `AIGovernDashboardDesign/design-summary-v1.md`
- `AIGovernDashboardDesign/dashboard-ia-v1.md`
- `AIGovernDashboardDesign/dashboard-columns-v1.md`
- `AIGovernDashboardDesign/homepage-design-decisions-v1.md`
- `AIGovernDashboardDesign/homepage-overview-mockup-v1.html`
- `AIGovernDashboardDesign/data-and-privacy-domain-mockup-v1.html`


## 来自作者的设计要求 - 需要遵守的最高优先级，此段内容禁止AI修改，只能人工修改。
1. 本项目是个POC，不考虑生产应用所必须的非功能性需求。
2. 用户操作流程：
    a) 首先要求用户登录，登陆后用户的 Entra ID 用户账户 显示在 登录按钮下，登录按钮变为 切换用户按钮（直接弹账号选择）
    b) 登陆后，显示1级页面，用户如果在1级页面点击链接，则跳转至对应的2级页面。
    c) 1, 2级页面都共享用户的登录信息。默认 都是 Time: Last 4 Weeks，支持 4 周 / 12 周切换。
    d) 每个页面都含有很多指标，页面打开后采用异步加载模式，逐步填充页面中的数字，列表，和图形。（页面打开后，逐个调用API加载数据）。
    e) 系统无管理员后台维护功能。
    f) UI 仅使用英文。
3. 本系统没有自己的数据库，但是会调用其他系统的数据库或API以获取数据
4. 按照 AIGovernDashboardDesign 目录下的：data-and-privacy-domain-mockup-v1.html 和 homepage-overview-mockup-v1.html 为蓝本设计UI
5. 前端使用 HTML5，Bootstrap，原生JS。FastAPI 直接托管静态 HTML/CSS/JS。后端使用HTTP的无状态的服务，使用Python，FastAPI开发，无需考虑高可靠，和性能要求。前端后端采用同一个 Python 程序。为每个指标，或者每个需要的前端数据，提供对应的API，API要求无状态。
6. 系统涉及到的数据库都是 Azure SQL Database，认证方式是 Entra ID Only，认证方式是基于 Entra ID 上的 Enterprise Application 的 Application(client) ID 和 client secret。
7. 应用程序基于 Entra ID 的 Enterprise Application 账户运行，用户使用Entra ID的用户账户登录，登录后，用户的账户不透传到数据层。应用程序使用 Client ID 及 App Secret访问数据层或AI服务。Redirect 要配置测试环境的地址，以及生产环境的地址。
8. 测试直接在开发使用的 Linux 服务器上直接完成，开发服务器上直接安装必要的环境，测试时，应用服务都直接使用 bash 命令在开发机Linux服务器上开启服务，无需发布到部署环境。测试采用 HTTP。
9. 开发代码的时候，对于环境变量的命名，有限参考并使用 .env.local 文件中已有的变量。
10. 每个代码文件顶端提供简单的注释
11. 根据需要开发的脚本文件，也在顶端提供注释
12. 生产环境到 Azure Web App 后通过平台提供的 HTTPS 对外提供服务。使用平台证书，不适用 azure keyvault
13. 环境变量使用 Azure Web App 的配置实现环境变量的注入，帮我生成基于 Linux 的 Azure CLI 脚本来配置 Azure Web App 的环境变量设置。
14. 对于错误处理，出现的错误打印到控制台，并且尽可能把错误导出到UI界面。
15. 对于重试机制，不需要建设备用的调用链路，失败就向控制台及UI返回报错即可。
16. 所有运行期需要的变量使用 环境变量传入。

