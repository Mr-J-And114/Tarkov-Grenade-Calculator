# Tarkov Grenade Calculator / 塔科夫榴弹射击辅助

A small ballistic calculator for grenade launcher usage in **Escape from Tarkov**.  
一个用于《逃离塔科夫》的榴弹弹道辅助计算器。

This tool supports grenade launcher ballistic calculation with **muzzle velocity + Ballistic Coefficient + ammo-specific drag coefficient K**, including elevation angle, azimuth, dynamic firing table, and height estimation by angle or scope mil/mrad.  
本工具支持基于 **初速 + Ballistic Coefficient 弹道系数 + 弹药专属阻力系数 K** 的榴弹弹道计算，包括俯仰角、方位角、动态射表，以及通过角度或瞄准镜密位估算高度差。

> Current version only calculates ballistic-related data. Damage, penetration, explosion radius, fragmentation, and other terminal-effect calculations have been removed.  
> 当前版本只计算弹道相关内容，已移除伤害、穿透、爆炸范围、破片等终端效果计算。

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

## 视频教程

```text
https://www.bilibili.com/video/BV1eE7X6QEyS/
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

## Major Update / 主要更新

The calculator no longer uses the old vacuum projectile formula as the main ballistic model.  
计算器不再将旧版无空气阻力抛体公式作为主要弹道模型。

The current version calculates grenade ballistic behavior from:  
当前版本根据以下参数计算榴弹弹道：

```text
Muzzle Velocity
Ballistic Coefficient
Ammo-specific drag coefficient K
Gravity

初速
弹道系数 BC
弹药专属阻力系数 K
重力
```

Velocity decay and time of flight are dynamically calculated from formulas.  
速度衰减与飞行时间由公式动态计算。

Elevation angles are solved through 2D drag trajectory simulation and numerical root finding.  
俯仰角通过二维阻力弹道积分与数值求根计算。

Damage and penetration estimation has been removed to keep the project focused on trajectory calculation.  
伤害与穿透估算已被移除，使项目专注于弹道计算。

---

## Built-in Ammo Presets / 内置弹药预设

Current built-in presets:  
当前内置预设：

| Ammo / 弹药 | Muzzle Velocity / 初速 | BC | Drag K / 阻力系数 K |
|---|---:|---:|---:|
| AGS-30 | 185 m/s | 0.316 | 0.000135 |
| VOG-25 | 76 m/s | 0.204 | 0.000160 |
| 40×46mm | 76 m/s | 0.204 | 0.000160 |
| Custom | User-defined / 用户自定义 | User-defined / 用户自定义 | User-defined / 用户自定义 |

VOG-25 and 40×46mm currently use the same ballistic parameters.  
VOG-25 与 40×46mm 当前使用一致的弹道参数。

Different ammunition uses different `K` values because projectile weight, shape, drag behavior, and in-game ballistic behavior are different.  
不同弹药使用不同的 `K` 值，因为弹药重量、弹体外形、阻力特性以及游戏内弹道表现不同。

The `K` values used here are **reverse-engineered correction coefficients** based on observed / calibrated ballistic behavior, not official real-world data or confirmed internal game-file values.  
这里使用的 `K` 值是根据观测 / 校准弹道表现 **反推得到的修正系数**，并非官方现实数据，也并非已确认的游戏文件内部数值。

---

## Features / 功能

### 1. Distance + Height Difference Mode / 距离与高低差模式

Calculate elevation angle by horizontal distance and height difference.  
根据水平距离和高低差计算俯仰角。

This mode uses the drag ballistic model:  
该模式使用阻力弹道模型：

```text
Muzzle Velocity + BC + K
初速 + BC + K
```

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

The program outputs:  
程序输出：

```text
Low-arc elevation angle
High-arc elevation angle if available
Estimated impact velocity
Estimated time of flight

低弹道俯仰角
高弹道俯仰角，如可用
估算命中速度
估算飞行时间
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

### 3. Dynamic Firing Table Mode / 动态射表模式

Generate a dynamic horizontal firing table from **0 to 1000 meters**.  
生成 **0 到 1000 米** 的动态水平面射表。

The table is calculated from current ammo parameters instead of hardcoded old reference cards.  
射表由当前弹药参数动态计算，不再依赖旧版硬编码参考射表。

Default condition:  
默认条件：

```text
Target and launcher are at the same height
目标和炮位处于同一水平面

Height difference = 0
高低差 = 0
```

The dynamic firing table includes only ballistic-related data:  
动态射表只包含弹道相关数据：

```text
Range
Low-arc elevation angle
High-arc elevation angle
Velocity
Time of flight
Zero-angle drop

距离
低弹道俯仰角
高弹道俯仰角
速度
飞行时间
水平射击下坠
```

The table no longer includes:  
射表不再包含：

```text
Estimated damage
Estimated penetration

估算伤害
估算穿透
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

### 5. Custom Ballistic Parameters / 自定义弹道参数

The user can temporarily customize ballistic parameters for testing or different ammunition types.  
用户可以临时自定义弹道参数，用于测试或适配不同弹药。

Customizable parameters:  
可自定义参数：

```text
Muzzle velocity
Ballistic Coefficient
Drag coefficient K

炮弹初速
Ballistic Coefficient / 弹道系数 BC
阻力系数 K
```

After applying custom parameters, the ammo preset switches to `Custom`.  
应用自定义参数后，弹药预设会切换到 `Custom`。

This setting is not saved after closing the program.  
该设置不会在关闭程序后保存。

---

### 6. Restore Default AGS Data / 恢复默认 AGS 数据

Restore the default AGS-30 ballistic data.  
恢复默认 AGS-30 弹道数据。

Default AGS-30 data:  
默认 AGS-30 数据：

```text
Muzzle velocity = 185 m/s
BC = 0.316
K = 0.000135

初速 = 185 m/s
BC = 0.316
K = 0.000135
```

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

The language text is stored in the program dictionary and can be extended in the future.  
语言文本存储在程序字典中，后续可以继续扩展。

---

## Ballistic Model / 弹道模型

### 1. Velocity Decay Formula / 速度衰减公式

The current version uses exponential velocity decay based on muzzle velocity, BC, and ammo-specific K:  
当前版本使用基于初速、BC 和弹药专属 K 值的指数速度衰减：

```text
v(x) = v0 × exp[-(K / BC) × x]
```

Where:  
其中：

```text
v(x) = velocity at distance x
v0 = muzzle velocity
K = ammo-specific drag coefficient
BC = Ballistic Coefficient
x = distance

v(x) = 距离 x 处速度
v0 = 初速
K = 弹药专属阻力系数
BC = 弹道系数
x = 距离
```

---

### 2. Time of Flight Formula / 飞行时间公式

Time of flight is calculated by integrating the velocity decay formula:  
飞行时间由速度衰减公式积分得到：

```text
t(x) = [exp((K / BC) × x) - 1] / [(K / BC) × v0]
```

Where:  
其中：

```text
t(x) = time of flight to distance x
v0 = muzzle velocity
K = ammo-specific drag coefficient
BC = Ballistic Coefficient
x = distance

t(x) = 到达距离 x 的飞行时间
v0 = 初速
K = 弹药专属阻力系数
BC = 弹道系数
x = 距离
```

If `K` is zero, the formula falls back to:  
如果 `K` 为零，则退化为：

```text
t = x / v0
```

---

### 3. 2D Drag Trajectory Simulation / 二维阻力弹道积分

Elevation angle calculation uses a 2D drag trajectory simulation.  
俯仰角计算使用二维阻力弹道积分。

Initial state:  
初始状态：

```text
vx = v0 × cos(θ)
vy = v0 × sin(θ)
x = 0
y = 0
```

Speed:  
速度：

```text
speed = sqrt(vx² + vy²)
```

Acceleration:  
加速度：

```text
ax = -(K / BC) × speed × vx
ay = -g - (K / BC) × speed × vy
```

Where:  
其中：

```text
g = 9.81 m/s²
```

The program numerically integrates the trajectory and searches for angles that make:  
程序对轨迹进行数值积分，并搜索满足以下条件的角度：

```text
simulated_y_at_target_distance = target_height_difference
模拟弹道在目标水平距离处的高度 = 目标高低差
```

The solver uses scan + bisection to find:  
求解器使用扫描 + 二分法寻找：

```text
Low-arc solution
High-arc solution

低弹道解
高弹道解
```

---

## About Ammo-Specific K / 关于弹药专属 K

Although BC describes part of the projectile drag behavior, it is not enough to fully describe every grenade's in-game trajectory. Different ammunition may have different projectile weight, mass distribution, shape, drag response, and game-implementation details.  
虽然 BC 可以描述一部分弹体抗阻表现，但它不足以完整描述每一种榴弹在游戏内的弹道。不同弹药可能具有不同的弹药重量、质量分布、弹体外形、阻力响应以及游戏实现细节。

Therefore, this calculator uses an ammo-specific `K` correction coefficient together with BC.  
因此，本计算器在 BC 之外额外使用弹药专属的 `K` 修正系数。

Important note:  
重要说明：

```text
The K values in this project are reverse-engineered from observed/calibrated in-game ballistic behavior.
They are fitting/correction parameters used by this calculator.
They are not official real-world ballistic constants.
They are not confirmed internal game-file values.

本项目中的 K 值是根据游戏内观测/校准弹道表现反推得到的。
它们是本计算器使用的拟合/修正参数。
它们不是官方现实弹道常数。
它们也不是已确认的游戏文件内部数值。
```

Current examples:  
当前示例：

```text
AGS-30 uses K = 0.000135
VOG-25 / 40×46mm use K = 0.000160

AGS-30 使用 K = 0.000135
VOG-25 / 40×46mm 使用 K = 0.000160
```

Using a single global K for all ammunition will not accurately match different grenade trajectories.  
如果对所有弹药使用同一个全局 K，无法准确匹配不同榴弹的弹道。

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

The ballistic model is based on game-calibrated velocity decay, Ballistic Coefficient, reverse-engineered ammo-specific drag coefficient K, and numerical trajectory simulation.  
弹道模型基于游戏校准的速度衰减、Ballistic Coefficient、反推得到的弹药专属阻力系数 K 以及数值弹道积分。

The `K` values are reverse-engineered fitting parameters based on observed/calibrated in-game behavior, not official values.  
`K` 值是基于游戏内观测 / 校准弹道表现反推得到的拟合参数，并非官方数值。

Actual in-game results may be affected by map data accuracy, measurement error, game updates, projectile behavior, and other unknown factors.  
实际游戏内结果可能受到地图数据精度、测量误差、游戏更新、弹体行为以及其他未知因素影响。

This project is not affiliated with Battlestate Games or Tarkov.dev.  
本项目与 Battlestate Games 或 Tarkov.dev 无官方关联。
