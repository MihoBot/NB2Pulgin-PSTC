# NB2Pulgin-PSTC

### 简介

Make user whose words include "陪睡套餐"

将发言中包含“陪睡套餐”等关键词的用户进行禁言

### 安装

- 直接将文件clone到自创文件夹即可（懒狗）
- 需要pathlib库和yaml库
```
pip install pathlib
pip install yaml
```

### 使用

如简介中的字面意思


初次启动时会自动创建配置文件，成功后在控制台会有此提示

```
陪睡套餐Config文件创建成功，请按需调整配置项，路径:.Config/PSTC
```

Config分为四个内容:

```
CanMsg: [] #如可以禁言则回复的内容
CantMsg: [] #如不能禁言则回复的内容（例如非管理或触发人为同级权限及以上）
WLMsg: [] #白名单人员特有的回复
WhiteList: [] #白名单
```

可以按需填写，格式为:
```
CanMsg: ["Arg1"]
```
或
```
CanMsg: ["Arg1", "Arg2"]
```

- 如不填写Config，回复内容将使用内置回复内容
- 白名单为无条件不禁言，所以回复单独分出来
- 修改完Config后请重启NoneBot控制台
