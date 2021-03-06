<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="MedusaScan" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa%20Scan-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.7+-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.77-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >美杜莎扫描器</h1>

**请使用者遵守 [中华人民共和国网络安全法](http://www.cac.gov.cn/2016-11/07/c_1119867116.htm)，勿将Medusa项目用于非授权的测试，Medusa项目开发者不负任何连带法律责任。**

### 关于美杜莎

>本项目使用 `GPL`协议，未经授权，禁止使用商业用途。
>
>`bash`版已上线
>
>`Bot`版本已上线
>
>`Web`版开发中，敬请期待~


### 使用文档

```
https://www.ascotbe.com/Medusa
```

### 漏洞覆盖列表

```
https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory
```

### Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/0.76.gif?raw=true)


### `Bash`版使用说明

```bash
# 安装工具(ubuntu
apt-get install nmap
# 下载文件
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# 安装依赖
pip3 install -r Medusa.txt
# 使用扫描器
python3 MedusaScan.py -u www.ascotbe.com
```
### 加速下载

```bash
# 如果下载太慢可以使用代理
# 全局代理
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
# 国内仓库下载
git clone https://gitee.com/asc0t6e/Medusa.git
```



### 参数说明

|命令|参数个数|作用                              |备注                           |
|------|--------|----------------------------------|-------------------------------|
|-u    |1       |输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 |https://www.ascotbe.com  or https://192.168.0.1         |
|-a    |1       |指定头文件或使用随机头|具体使用参考使用文档|
|-f    |1       |需要批量扫描目标url所在文件名字|-u和-f只能存在一个，并且必须存在一个|
|-m    |1       |针对单独的模块进行扫描比如Struts2、Apache等|具体内容可以通过项目文件夹来输入|
|-t    |1       |设置线程数，默认线程数15||
|-sp    |1       |爆破数据库的密码字典|如果输入-sp和-su并且其中一个值为空，则使用默认密码爆破|
|-su    |1       |爆破数据库的用户字典|无|
|-s    |0       |通过DNS以及各大搜索引擎查找子域名|从Sublist3r魔改而来,不支持IP枚举|
|-se    |0       |包含了-s的功能，并且通过字典枚举(非常耗时|和-s不能同时使用，-s和-se只能存在一个|

### `Bot`版使用说明

```
# 下载文件
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# 安装依赖
pip3 install -r Medusa.txt
# 后续配置参考比如文档中的机器人模块
https://www.ascotbe.com/Medusa
```

### 更新日志

```
https://www.ascotbe.com/Medusa/Documentation/#/UpDataLog
```

### 复现文档

```
https://www.ascotbe.com/Loophole
```

### 提交意见

- 吹B群：**690021184**（加群请输入暗号：**6CF2D42B629E5AA4E6C293B290798878**）
- GitHub issue

### 友情链接

- [零组资料库](http://www.0-sec.org)

### 贡献人员

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)


### 时间轴

![star](https://starchart.cc/Ascotbe/Medusa.svg)






