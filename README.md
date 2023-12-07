# CodemaoAutoRegister

**编程猫全自动发码/穷举验证码注册工具**

如果可以的话,请点个Star~

## 🛎 更新文档

### 2023.12.7 (8)

将SendCaptcha文件移出了仓库,放到了GitHub Gist上 : https://gist.github.com/Wangs-official/c5203f3e57db0a88e6346b03746d8ad1

### 2023.11.25 (7)

加入了穷举验证码 ^_^ 虽然不知道能不能真穷举出来,总之能用就行

### 2023.11.25 (6)

发现了API风控的样子,返回信息从`{"rule":"DEFAULT","appid":"","ticket":"xxx"}(未风控)`变成了`{"rule":"TENCENT","appid":"xxx"}`

至少还能风控已经很棒了,这个版本加上了自动检测风控,遇到风控会自动停止,不会继续运行

> 实测会在发码量达到500时触发风控

## 🤔 最新の小发现

1. 还有一个发码API是`https://dev-open-service.codemao.cn/captcha/rule`,请求方式以及数据与`https://open-service.codemao.cn/captcha/rule/v3`相同,没看出来他俩的区别

## 💻 依赖

项目使用Python构建,依赖`requests`和`fake_useragent`库,请在开始使用前执行该命令(已经安装的可以忽略)

```bash
pip3 install requests
pip3 install fake-useragent
```

## 😋 什么是CodemaoAutoRegister?

全自动穷举验证码,你还在为绑定手机号烦恼?可笑

## 🕹 在本地使用

1. 克隆并cd到仓库内
2. 执行以下指令
- 发一个码

```bash
python3 SendOneCaptcha.py -p <手机号码>
```

- 开始穷举验证码

```bash
python3 TestCaptchaCode.py -p <手机号码> -w <等待时间(单位秒)>
```

> ⚠️ 请先使用`python3 SendOneCaptcha.py -p <手机号码>`命令发码!验证码有效期为10分钟,程序已限制运行时间为10分钟,请及时开始穷举验证码

## ☁️ 在云端运行

因为一些原因我们必须隐藏自己的IP,云端是个不错的选择

在座的各位想必都玩过AI画图,所以对笔记本这东西(.ipynb)肯定很熟悉,直接拖入到Jupyter notebook里就可以使用了,有网络条件(指出国)的可以用Google Colab,在这里我就不多说了

[Open In Colab](https://colab.research.google.com/github/Wangs-official/CodemaoAutoRegister/blob/main/CodemaoAutoRegister.ipynb)

## 🌏 API

### 发码API

- API地址:`https://open-service.codemao.cn/captcha/rule/v3`
- 请求方式:POST
- 请求数据(均为必填):

|    键     |  类型  |             备注             |
| :-------: | :----: | :--------------------------: |
| deviceId  | string |         生成UUID即可         |
| identity  |  int   |           手机号码           |
|    pid    | string | 大概是官网用于记录登录时所在平台用的,65edCTyg是社区的PID |
|   scene   |   ？   |        未知，默认为空        |
| timestamp | string |          请求时间戳          |

### 验证API

- API地址:`https://api.codemao.cn/tiger/v3/web/accounts/register/phone/with-agreement`
- 请求方式:POST
- 请求数据(均为必填):

|      键       |  类型  |             备注             |
| :-----------: | :----: | :--------------------------: |
| phone_number  |  int   |           手机号码           |
|   password    | string |             密码             |
|    captcha    | string |            验证码            |
| agreement_ids |  list  |        默认`[12,13]`         |
|      pid      | string | 大概是官网用于记录登录时所在平台用的,65edCTyg是社区的PID |

## 🧠 性能

实体机的CPU为:`2.7 GHz 四核Intel Core i7`

测试网络环境: `中国电信4G`

测试线程: `8线程` 间隔时间:`1秒`

在网络正常且无波动的情况下,实际可运行次数为:4769次

任何人的设备都不一样,所以我不确定所有人的设备都能运行到这个数量,可能会有波动,请以自己的设备为准


## 😱 免责声明

仅供学习交流使用!请在24H内删除,若侵犯了您的权益,请联系我QQ:1480357968

___


> "花开花落暗示着呼应着我，茫茫荒漠顷刻间春夏秋冬" 来自: 育空河 - 咩栗 https://music.163.com/song?id=2019299993
