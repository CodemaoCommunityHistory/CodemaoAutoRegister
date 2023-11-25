# CodemaoAutoRegister

**编程猫全自动发码/穷举验证码注册工具**

如果可以的话,请点个Star~

## 🛎 更新文档

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

技术宅迟早毁了BCM,这是Wangs说的

某一天Wangs突发奇想,要不要狠狠地坑一把编程猫? 毕竟现在编程猫半死不活的,坑一把又不能找我来XD

所以Wangs打开了抓包软件,特别巧,包一抓就抓到了,然后Wangs又写了一个简简单单的Python程序重复发包,没想到猫站不仅没有人机验证(特别是发码要花钱的场景),还没有限制!令人忍俊不禁

Wangs知道之后非常开心,再大笑毛毡您连钱都不管了的同时顺便在Nemo小宇宙里大肆谈论,也不知道毛毡那边的看见没有~

互联网精神影响着Wangs,所以他就把自己的发现开源了,快说谢谢Wangs!()

## 🕹 在本地使用

1. 克隆并cd到仓库内
2. 执行以下指令

- 开始循环发码

```bash
python3 SendCaptcha.py -w <间隔时间(单位秒)> -ru <随机UA(True/False)>
```

- 发一个码

```bash
python3 SendOneCaptcha.py -p <手机号码>
```

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

## 😱 免责声明

仅供学习交流使用!请在24H内删除,若侵犯了您的权益,请联系我QQ:1480357968

___


> "花开花落暗示着呼应着我，茫茫荒漠顷刻间春夏秋冬" 来自: 育空河 - 咩栗 https://music.163.com/song?id=2019299993
