# Kuro Overlay
《蔚蓝档案》黑白ins总力战安定点提示工具

## 下载
在 [release 页面](https://github.com/raphaeIl/KuroOverlay/releases) 下载 exe

## 使用
双击 `kuro_overlay.exe`

点击 `t` (默认) 即可打开和关闭安定点提示页面
点击 `c` 可切换安定点图 (目前只有两张)

[其他教程](#教程)

## 配置要求
* windows pc （目前不支持手机）
* 16:9 屏幕分辨率 (1920x1080最佳)
* 蓝叠模拟器（其他的应该也可以）
* 首先你得能凹到 p2 ～(≧ ∇ ≦)/

## 展示
页面

![alt text](https://github.com/raphaeIl/KuroOverlay/blob/main/preview/preview.png)

[视频展示+教学](https://www.bilibili.com/video/BV1vu4m1w7oe)

#### 教程

据我自己测试，忍忍的技能需要放到下图显示的位置才能避免伤害

![alt text](https://github.com/raphaeIl/KuroOverlay/blob/main/preview/preview2.png)

目前有两张图, 个人感觉第二张更稳, 可以都试试 那张用起来手感好就用那张

图因为是我扒的所以不太好 如果有大佬有更精准的图 球球发给我 ～(≧ ω ≦)

## 自定义快捷键
下载或创建 `config.json` 并放入exe所在文件夹

模板：
```
{
    "toggle_key": "t",
    "switch_key": "c",
    "overlay_opacity": 0.5
}
```

- `toggle_key`: 开启/关闭 页面快捷键
- `switch_key`: 切换安定点图
- `overlay_opacity`: 页面透明度

## 注释
目前(好像) 只能用于ins难度

[安定点图](https://twitter.com/Midokuni_Mido/status/1575152057438261248) - 感谢 
[Midokuni](https://twitter.com/Midokuni_Mido) 大佬

作者：[Raphael](https://space.bilibili.com/1270793735) 

脚本未修改任何游戏数据，可以放心使用，有问题请b站私信或开issues

## ChangeLog
`v0.0.1`: Initial Release

`v0.0.2`: Added the ability to swap overlays
