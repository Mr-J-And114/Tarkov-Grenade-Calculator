# Tarkov Grenade Calculator / 塔科夫榴弹射击辅助

A small ballistic calculator for grenade launcher usage in **Escape from Tarkov**.  
一个用于《逃离塔科夫》的榴弹弹道辅助计算器。

This tool is mainly designed for AGS grenade launcher calculations, including elevation angle, azimuth, firing table, and height estimation by angle or scope mil/mrad.  
本工具主要用于 AGS 榴弹发射器相关计算，包括俯仰角、方位角、射表，以及通过角度或瞄准镜密位估算高度差。

---

## Author / 作者

**Mr.J.And**

---

## Repository / 仓库

**Mr-J-And114/Tarkov-Grenade-Calculator**

GitHub repository:  
GitHub 仓库：

```text
https://github.com/Mr-J-And114/Tarkov-Grenade-Calculator
```

---

## Map Coordinate Source / 地图坐标来源

Coordinates are currently obtained from Tarkov.dev maps:  
坐标数据目前来自 Tarkov.dev 地图：

```text
https://tarkov.dev/maps/
```

You can use Tarkov.dev maps to obtain launcher and target coordinates, then input them into the coordinate calculation mode.  
你可以通过 Tarkov.dev 地图获取炮位和目标坐标，然后输入到坐标计算模式中。

---

## Features / 功能

### 1. Distance + Height Difference Mode / 距离与高低差模式

Calculate elevation angle by horizontal distance and height difference.  
根据水平距离和高低差计算俯仰角。

Height difference rule:  
高低差规则：

```text
Height difference = target height - launcher height
高低差 = 目标高度 - 炮位高度
```

Positive value means the target is higher than the launcher.  
正数表示目标比炮位高。

Negative value means the target is lower than the launcher.  
负数表示目标比炮位低。

Example:  
示例：

```text
Target is 20m higher: input 20
目标比炮位高 20 米：输入 20

Target is 35m lower: input -35
目标比炮位低 35 米：输入 -35
```

---

### 2. Coordinate Calculation Mode / 坐标计算模式

Calculate horizontal distance, azimuth, and elevation angle by launcher and target coordinates.  
根据炮位坐标和目标坐标计算水平距离、方位角和俯仰角。

Input rule:  
输入规则：

```text
First point = launcher position
前者 = 炮位

Second point = target position
后者 = 目标
```

The program calculates the height difference by:  
程序通过以下方式计算高低差：

```text
Height difference = target Z - launcher Z
高低差 = 目标 Z - 炮位 Z
```

Because some electronic map coordinate axes may not match real map directions, the program provides a manual direction correction option.  
由于部分电子地图坐标轴可能与实际地图方向不完全一致，程序提供了手动方位修正选项。

Supported relative directions:  
支持的相对方位：

```text
North / 北
North-East / 东北
East / 东
South-East / 东南
South / 南
South-West / 西南
West / 西
North-West / 西北
```

Azimuth definition:  
方位角定义：

```text
North = 0°
East  = 90°
South = 180°
West  = 270°

正北 = 0°
正东 = 90°
正南 = 180°
正西 = 270°
```

---

### 3. Firing Table Mode / 射表模式

Generate a horizontal firing table from **0 to 1000 meters**.  
生成 **0 到 1000 米** 的水平面射表。

Default condition:  
默认条件：

```text
Target and launcher are at the same height
目标和炮位处于同一水平面

Height difference = 0
高低差 = 0
```

If the target is higher or lower than the launcher, do not directly use the horizontal firing table. Use Distance + Height Difference Mode or Coordinate Calculation Mode instead.  
如果目标与炮位存在高低差，不建议直接套用水平射表，应使用“距离与高低差模式”或“坐标计算模式”。

---

### 4. Angle/Mil Height Estimation Mode / 角度与密位测高模式

Estimate target height difference by observation angle or scope mil/mrad.  
根据观测角度或瞄准镜密位估算目标相对观测点的高度差。

This mode is useful when you can measure the angle or scope mil value between your horizontal line and the target.  
当你可以测量目标相对水平线的角度或瞄准镜密位时，可以使用该模式估算高度差。

Supported angle units:  
支持的角度单位：

```text
Degree
Mil / mrad

度
密位 / 毫弧度
```

Supported distance types:  
支持的距离类型：

```text
Slant Range
Horizontal Range

直线距离 / 斜距
水平距离
```

If the known distance is **slant range**, use:  
如果已知距离是 **直线距离/斜距**，使用：

```text
height = range × sin(angle)
高度差 = 距离 × sin(角度)
```

If the known distance is **horizontal range**, use:  
如果已知距离是 **水平距离**，使用：

```text
height = range × tan(angle)
高度差 = 距离 × tan(角度)
```

Angle sign rule:  
角度正负规则：

```text
Positive angle = target is above the observer's horizontal line
Negative angle = target is below the observer's horizontal line

正角度 = 目标在观测者水平线上方
负角度 = 目标在观测者水平线下方
```

Mil/mrad conversion:  
密位/毫弧度换算：

```text
1 mil = 1 mrad = 0.001 rad
radian = mil / 1000

1 密位 = 1 毫弧度 = 0.001 弧度
弧度 = 密位 / 1000
```

The program also supports sight height input.  
程序也支持输入瞄准镜或观测设备离地高度。

This can be used to estimate the target height relative to the observer's ground position.  
这可以用于估算目标相对观测点地面的高度。

```text
target height from observer ground = calculated height difference + sight height
目标相对观测点地面高度 = 计算出的高度差 + 瞄准镜离地高度
```

---

### 5. Temporary Projectile Velocity Override / 临时覆盖炮弹初速

The projectile velocity can be temporarily changed for testing or different ammunition types.  
可以临时修改炮弹初速，用于测试或适配不同弹药。

This setting is not saved after closing the program.  
该设置不会在关闭程序后保存。

---

### 6. Restore Default AGS Data / 恢复默认 AGS 数据

Restore the default AGS equivalent projectile velocity calculated from the default calibration point.  
恢复由默认校准点反推出的 AGS 等效炮弹初速。

---

### 7. Language Switching / 语言切换

The program supports language switching between:  
程序支持以下语言切换：

```text
Chinese
English

中文
英文
```

The language text is stored in independent language modules, making it easier to add more languages in the future.  
语言文本以独立模块方式存储，方便后续继续增加更多语言。

---

## Default AGS Calibration / 默认 AGS 校准数据

Default calibration point:  
默认校准点：

```text
300m = 2.5°
```

Gravity used by the calculator:  
程序使用的重力加速度：

```text
g = 9.81 m/s²
```

The default equivalent projectile velocity is calculated from the calibration point.  
默认等效初速由该校准点反推得到。

> Note: This velocity is based on in-game measured calibration data. It may not match real-world weapon data or internal game file data.  
> 注意：该初速基于游戏内实测校准数据反推，不一定等于现实武器数据或游戏文件内部数据。

---

## Ballistic Formula / 弹道公式

### Same-Height Range Formula / 同水平面射程公式

```text
R = v² / g × sin(2θ)
```

Where:  
其中：

```text
R = range
v = projectile velocity
g = gravity
θ = elevation angle

R = 射程
v = 炮弹初速
g = 重力加速度
θ = 俯仰角
```

---

### Trajectory Formula With Height Difference / 有高低差弹道公式

```text
h = x × tan(θ) - g × x² / [2 × v² × cos²(θ)]
```

Solving for `tan(θ)`:  
解出 `tan(θ)`：

```text
tan(θ) = [v² ± sqrt(v⁴ - g(gx² + 2hv²))] / gx
```

Where:  
其中：

```text
x = horizontal distance
h = height difference = target height - launcher height
v = projectile velocity
g = gravity
θ = elevation angle

x = 水平距离
h = 高低差 = 目标高度 - 炮位高度
v = 炮弹初速
g = 重力加速度
θ = 俯仰角
```

Low-arc solution uses the minus sign.  
低弹道解使用减号。

High-arc solution uses the plus sign.  
高弹道解使用加号。

In most practical cases, the low-arc solution is recommended.  
多数实战情况下，推荐优先使用低弹道解。

---

## Height Estimation Formula / 测高公式

### Known Slant Range / 已知直线距离或斜距

```text
height = slant_range × sin(angle)
```

```text
高度差 = 直线距离 × sin(角度)
```

---

### Known Horizontal Range / 已知水平距离

```text
height = horizontal_range × tan(angle)
```

```text
高度差 = 水平距离 × tan(角度)
```

---

### Mil/mrad Conversion / 密位换算

```text
radian = mil / 1000
```

```text
弧度 = 密位 / 1000
```

For small angles, this approximation is also commonly usable:  
在小角度情况下，也可以近似估算：

```text
height ≈ distance × mil / 1000
```

```text
高度差 ≈ 距离 × 密位 / 1000
```

---

## Build EXE / 打包 EXE

Install PyInstaller:  
安装 PyInstaller：

```bash
python -m pip install pyinstaller
```

Build:  
打包：

```bash
python -m PyInstaller -F -w -n "Tarkov-Grenade-Calculator" tarkov_grenade_calculator.py
```

If `python` is not available, try:  
如果 `python` 命令不可用，可以尝试：

```bash
py -m PyInstaller -F -w -n "Tarkov-Grenade-Calculator" tarkov_grenade_calculator.py
```

The generated executable will be located in:  
生成的可执行文件位于：

```text
dist/
```

---

## Disclaimer / 免责声明

This tool is made for calculation, testing, and learning purposes.  
本工具仅用于计算、测试和学习用途。

The ballistic model is based on simplified projectile motion and in-game calibration data.  
弹道模型基于简化抛体运动和游戏内校准数据。

Actual in-game results may be affected by map data accuracy, measurement error, game updates, projectile behavior, and other unknown factors.  
实际游戏内结果可能受到地图数据精度、测量误差、游戏更新、弹体行为以及其他未知因素影响。

This project is not affiliated with Battlestate Games or Tarkov.dev.  
本项目与 Battlestate Games 或 Tarkov.dev 无官方关联。
