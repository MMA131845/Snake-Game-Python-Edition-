<div align="center">
<font color="red" size="7"><b>已停止开发</b></font>
</div>

# Snake-Game-Python-Edition-

<div align="center">

**自由贪吃蛇 · Python 版**

*Multi-Mode · AI Opponents · Pygame Rendering · IPC Bridge · Team Battle*

[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-0078D4?style=flat-square&logo=windows)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-00A800?style=flat-square)](https://www.pygame.org/)
[![Version](https://img.shields.io/badge/version-5.2.3-00b7c3?style=flat-square)](https://github.com/MMA131845/Snake-Game-Python-Edition-/releases)
[![License](https://img.shields.io/badge/license-MIT-00cc6a?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MMA131845/Snake-Game-Python-Edition-?style=flat-square&color=ff763b)](https://github.com/MMA131845/Snake-Game-Python-Edition-/stargazers)

[功能特性](#-功能特性) · [快速开始](#-快速开始) · [游戏模式](#-游戏模式) · [架构设计](#-架构设计) · [版本演进](#-版本演进) · [配套启动器](#-配套启动器)

</div>

---

## 项目简介

**Snake-Game-Python-Edition-** 是「自由贪吃蛇」系列的 Python 实现版本，经历了从 **turtle 图形库** 到 **Pygame 引擎** 的完整架构演进，最终形成一套具备 **多种游戏模式**、**智能 AI 对手**、**团队竞技**、**反作弊通信** 的完整游戏系统。

游戏通过 **命名管道（Named Pipe）** 与配套启动器 SnakeLauncherWPF 建立实时通信，将 FPS、得分、击杀、模式等状态上报给启动器；同时采用 **HMAC-SHA256 消息签名** 与 **时间戳防重放** 机制，与启动器共享同一套反作弊协议。

> **设计哲学**：Python 生态的灵活性 + 现代游戏引擎的表现力 = 一款可以持续演进的游戏。

### 项目定位

| 维度 | 描述 |
|:----:|:-----|
| **目标玩家** | 贪吃蛇爱好者、多模式挑战者、竞技对抗玩家 |
| **核心价值** | 跨引擎演进、多模式支持、IPC 集成、反作弊 |
| **技术标签** | Python · Pygame · Named Pipe · HMAC · 团队 AI |
| **代码规模** | 单文件脚本，~3000 行 Python |

---

## 功能特性

### 游戏管理

<table>
<tr>
<td width="50%">

**多种游戏模式**
- 经典模式（Classic）：传统贪吃蛇玩法
- 淘汰之王（Timed）：100 名 AI 大混战
- 占领模式（Team 4v4）：与蓝队 AI 合作占领中央据点
- 搜打撤（Mojin）：三角洲行动风格撤离玩法

</td>
<td width="50%">

**智能 AI 对手**
- AI 主动觅食，行为接近真人
- 追击 / 躲避自适应决策
- 绕前拦截与包抄攻击
- 团队模式下的阵营协同
- AI 之间也会互相击杀

</td>
</tr>
</table>

### 战斗与道具系统

| 系统 | 描述 |
|:-----|:-----|
| **加速** | 长按 Ctrl 加速 5 秒，冷却后再次可用 |
| **容器** | 搜打撤模式中可搜索的补给箱，产出分数 / 食物 / 加速 |
| **击杀掉落** | 敌人死亡时按身体长度掉落红色大食物 |
| **食物聚集** | 同色食物概率聚集在相同区域，增加拾取效率 |
| **实时排名** | 淘汰之王模式右上角显示前 15 名 |
| **成就系统** | 初次击杀 / 十人斩 / 五十人斩 / 常胜将军 / 生存专家 / 占领专家 |

### IPC 通信与反作弊

- **Named Pipe 上报** — 每 0.5 秒向启动器推送一次状态
- **HMAC-SHA256 签名** — 与启动器共享 32 字节密钥
- **时间戳参与签名** — 30 秒容忍窗口，防止重放攻击
- **格式**：`FPS:{fps},SCORE:{score},KILLS:{kills},MODE:{mode},TS:{ts},SIG:{hmac}`

### 画面设置

- **21 种分辨率** — 从 800×600 到 3840×2160
- **3 种显示模式** — 无边框全屏 / 窗口化（无边框） / 窗口化
- **5 种界面主题** — 白色 / 浅灰 / 浅蓝 / 浅绿 / 浅粉
- **5 档帧率上限** — 30 / 60 / 120 / 144 / 240
- **自适应缩放** — 基于 1600×900 基准比例缩放所有元素

### 自定义选项

- **背景样式**：纯黑 / 纯白 / 格子 / 星空
- **蛇头颜色**：浅绿 / 黄 / 橙 / 粉 / 青 / 白
- **蛇身颜色**：绿 / 深绿 / 蓝 / 紫 / 棕 / 灰
- **名字输入**：首次启动时引导输入玩家名称（最多 20 字符）

---

## 游戏模式

### 经典模式（Classic）

最传统的贪吃蛇玩法。

- **食物数量**：125 个
- **敌人数量**：10 个
- **AI 行为**：主动觅食，遇到玩家时按体型决定攻击/躲避
- **加速**：Ctrl 键，5 秒内速度 ×2
- **碰撞死亡**：撞墙 / 撞敌人身体 / 撞自身身体

### 淘汰之王（Timed）

100 名 AI 大混战。

- **AI 数量**：100 个
- **AI 行为**：
  - 分数 < 20：优先躲避玩家
  - 分数 ≥ 20 且未进入攻击阶段：躲避 + 觅食
  - 狂暴阶段（≥15 名 AI 达到 20 分触发）：集体攻击玩家
- **攻击策略**：10 种不同战术（绕前、包抄、正面冲锋等）
- **实时排名**：右上角显示前 15 名
- **击杀记录**：击杀 AI 后掉落对应分数的大食物

### 占领模式（Team 4v4）

4v4 团队竞技，占领中央据点。

- **队伍构成**：蓝队（玩家 + 3 AI）vs 红队（4 AI）
- **地图尺寸**：1000 × 800
- **占领机制**：站在圈内推进进度条，30 秒内推满获胜
- **AI 协同**：
  - 有队友占点时主动攻击敌人
  - 无人占点时回防据点
  - 顺路会吃食物
- **敌人重生**：被击杀后 3 秒复活，保持持续压力
- **共享分数**：队友击杀敌人玩家也得分

### 搜打撤（Mojin）

三角洲行动风格撤离玩法。

- **地图**：三张可选地图（废弃工厂 / 边境森林 / 航天基地）
- **容器搜索**：靠近容器按 F 搜索，完成后再按 F 拾取
- **奖励类型**：分数 / 食物 / 加速
- **撤离条件**：站在撤离点 9 秒
- **危险**：航天基地有红色燃烧弹范围（停留 5 秒死亡）
- **仓库系统**：拾取的物资存入仓库，跨局保留

---

## 快速开始

### 环境要求

| 组件 | 最低版本 | 推荐版本 |
|:-----|:--------:|:--------:|
| Windows | 10 | 11 |
| Python | 3.8 | 3.11+ |
| Pygame | 2.0 | 2.6+ |
| pywin32 | 305 | 306+ |

### 安装与运行

```bash
# 1. 克隆仓库
git clone https://github.com/MMA131845/Snake-Game-Python-Edition-.git
cd Snake-Game-Python-Edition-

# 2. 安装依赖
pip install pygame pywin32

# 3. 运行游戏
python "贪吃蛇(5.2.3).py"
```

### 首次运行

1. 首次运行会弹出**版本更新日志**窗口，展示当前版本的新特性
2. 随后弹出**名字输入界面**，输入最多 20 字符的玩家名称
3. 进入主菜单，可选择游戏模式并开始游玩

### 操作指南

| 操作 | 功能 |
|:-----|:-----|
| **鼠标移动** | 控制蛇头方向（经典 / 淘汰之王 / 搜打撤） |
| **WASD** | 控制蛇头方向（占领模式） |
| **Ctrl（长按）** | 加速（5 秒限时） |
| **F** | 决斗（淘汰之王）/ 搜索容器（搜打撤） |
| **M** | 切换游戏模式 |
| **S** | 进入设置 |
| **H** | 查看排行榜 |
| **J** | 查看成就 |
| **R** | 重新开始 |
| **Q** | 退出游戏 |
| **Esc** | 暂停 / 返回上级 |

---

## 架构设计

### 模块划分

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐    │
│  │ 主菜单   │ │ 设置界面 │ │ 排行榜   │ │ 成就 / 日志 │    │
│  └──────────┘ └──────────┘ └──────────┘ └─────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                     Game Mode Layer                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐    │
│  │ Classic  │ │  Timed   │ │ Team 4v4 │ │   Mojin     │    │
│  └──────────┘ └──────────┘ └──────────┘ └─────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                       Core Layer                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐    │
│  │ 游戏循环 │ │  AI 决策 │ │ 碰撞检测 │ │  摄像机     │    │
│  └──────────┘ └──────────┘ └──────────┘ └─────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                    Infrastructure Layer                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐    │
│  │  IPC     │ │ 成就存储 │ │ 排行榜   │ │  版本检测   │    │
│  │ 管道通信 │ │  JSON    │ │  JSON    │ │ 版本文件    │    │
│  └──────────┘ └──────────┘ └──────────┘ └─────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 核心数据结构

```python
# 玩家蛇
snake = [(x0, y0), (x1, y1), ...]           # 头部索引 0
direction = (dx, dy)                         # 单位方向向量

# 敌人蛇
enemies = [
    {
        'body': [(x, y), ...],
        'dir': (dx, dy),
        'score': int,
        'name': str,
        'state': 'idle' | 'preparing' | 'attacking',
        'team': 'red' | 'blue'              # 团队模式
    },
    ...
]

# 食物
foods = [(x, y, color, radius), ...]

# 容器（搜打撤）
containers = [(x, y, radius, reward_type, reward_value), ...]
```

### 关键常量

| 常量 | 值 | 说明 |
|:-----|:--:|:-----|
| `BASE_SPEED` | 4.5 × SCALE | 初始速度 |
| `MIN_SPEED` | 2 × SCALE | 最低速度 |
| `SPEED_DECAY` | 0.016 / SCALE | 每分减速 |
| `FOOD_COUNT` | 125 | 食物总数 |
| `BOOST_DURATION` | 5.0 | 加速持续时间 |
| `BOOST_MULTIPLIER` | 2.0 | 加速倍数 |
| `CAPTURE_RADIUS` | 80 × SCALE | 占领半径 |
| `CAPTURE_TIME` | 30.0 | 占领所需时间 |

---

## 技术亮点

### 1. 跨引擎演进史

| 版本 | 引擎 | 关键特性 |
|:-----|:-----|:---------|
| 1.0.0 | Turtle | 基础玩法、鼠标控制 |
| 2.1.0 | Turtle | 摄像机跟随、大世界（3000×2000） |
| 2.10.0 | Turtle | 自定义蛇颜色、方格背景 |
| 3.0.0 | Pygame | 流畅渲染、60 FPS |
| 3.10.0 | Pygame | 淘汰之王模式 |
| 4.0.0 | Pygame | 搜打撤模式、Windows 11 风格 UI |
| 5.0.0 | Pygame | 团队 4v4、成就系统 |
| 5.2.3 | Pygame | IPC 通信、HMAC 签名 |

### 2. 自适应分辨率系统

```python
BASE_WIDTH, BASE_HEIGHT = 1600, 900
SCALE_X = SCREEN_WIDTH / BASE_WIDTH
SCALE_Y = SCREEN_HEIGHT / BASE_HEIGHT
SCALE = min(SCALE_X, SCALE_Y)

# 所有尺寸基于 SCALE 缩放
BASE_SPEED = 4.5 * SCALE
BASE_SEGMENT_RADIUS = int(8 * SCALE)
BUTTON_WIDTH = int(300 * SCALE)
```

- 支持 21 种分辨率（800×600 ~ 3840×2160）
- 切换分辨率时重建 `screen` 对象并重新计算所有常量
- 保持纵横比，UI 元素不失真

### 3. 摄像机跟随

```python
def update_camera(head_x, head_y):
    global cam_x, cam_y
    cam_x, cam_y = head_x, head_y
    # 限制摄像机范围，避免世界边界外露出空白
    min_cam_x = WORLD_MIN_X + SCREEN_WIDTH // 2
    max_cam_x = WORLD_MAX_X - SCREEN_WIDTH // 2
    if min_cam_x < max_cam_x:
        cam_x = max(min_cam_x, min(cam_x, max_cam_x))
```

**坐标转换**：

```python
def world_to_screen(wx, wy):
    return int(wx - cam_x + SCREEN_WIDTH // 2), int(wy - cam_y + SCREEN_HEIGHT // 2)

def screen_to_world(sx, sy):
    return sx - SCREEN_WIDTH // 2 + cam_x, sy - SCREEN_HEIGHT // 2 + cam_y
```

### 4. IPC 通信与 HMAC 签名

**PipeClient 类**（v5.2.3 中通过 `win32pipe` 与 `win32file` 实现）：

```python
import win32pipe, win32file, pywintypes

def ipc_worker():
    pipe_name = r'\\.\pipe\SnakeGameFPSPipe'
    while True:
        try:
            win32pipe.WaitNamedPipe(pipe_name, win32pipe.NMPWAIT_USE_DEFAULT_WAIT)
            handle = win32file.CreateFile(
                pipe_name,
                win32file.GENERIC_WRITE,
                0, None, win32file.OPEN_EXISTING, 0, None
            )
            while True:
                fps = int(clock.get_fps())
                current_score = score
                kills = game_stats["current_game_kills"]
                mode_str = game_mode
                line = f"FPS:{fps},SCORE:{current_score},KILLS:{kills},MODE:{mode_str}\n"
                win32file.WriteFile(handle, line.encode())
                time.sleep(0.5)
            win32file.CloseHandle(handle)
        except:
            pass
        time.sleep(2)
```

**HMAC 签名**（与启动器共享密钥）：

```python
RootKey = bytes([
    0xA3, 0x71, 0x0F, 0xC5, 0x2D, 0x88, 0xE6, 0x14,
    0x59, 0xBB, 0x93, 0x27, 0xF0, 0x44, 0x6A, 0xD8,
    0x1C, 0xE2, 0x75, 0x38, 0xAF, 0x06, 0x5B, 0x90,
    0x8D, 0x33, 0x4F, 0xCA, 0x11, 0x7E, 0x62, 0xB5
])

def compute_hmac(payload):
    import hmac as hmac_lib
    return hmac_lib.new(RootKey, payload.encode(), 'sha256').hexdigest()
```

### 5. AI 决策系统

```python
def get_enemy_new_direction(enemy, foods_list):
    old_dir = enemy['dir']
    head = enemy['body'][0]
    
    # 1. 碰撞规避（优先级最高）
    if will_collide_with_player(head, old_dir, radius):
        evade = get_evade_direction(head, all_segs, old_dir, radius)
        if evade:
            return evade
    
    # 2. 淘汰之王模式：狂暴阶段判断
    if game_mode == "timed":
        high_count = sum(1 for e in enemies if e['score'] >= 20)
        if not global_attack_phase and high_count >= attack_trigger_count:
            global_attack_phase = True
        
        # 根据分数选择行为
        if score_e < 20:
            return evade  # 躲避
        else:
            return attack_player(head, ...)  # 攻击
    
    # 3. 团队模式：配合与目标选择
    if game_mode == "team4v4":
        # 蓝队攻击红队基地，红队攻击蓝队基地
        ...
    
    # 4. 觅食
    if foods_list and random.random() < ENEMY_FOOD_SEEK_PROB:
        target = find_nearest_food(head, foods_list)
        if target:
            return direction_to(head, target)
    
    # 5. 随机漫游
    return random.choice(valid_directions)
```

**AI 工具函数**：

```python
def direction_will_collide(head, dir_vec, all_segments, radius, check_dist=60):
    """预测方向 60px 后是否会碰撞"""
    cx = head[0] + dir_vec[0] * check_dist
    cy = head[1] + dir_vec[1] * check_dist
    threshold = (radius * 2) ** 2
    return any((cx - sx)**2 + (cy - sy)**2 < threshold for sx, sy in all_segments)

def get_evade_direction(head, all_segments, old_dir, radius):
    """基于排斥力场的规避方向"""
    rep = [0.0, 0.0]
    for sx, sy in all_segments:
        dx, dy = head[0] - sx, head[1] - sy
        dist_sq = dx*dx + dy*dy
        if dist_sq < (radius*4)**2 and dist_sq > 0:
            force = 1.0 / (dist_sq + 1e-6)
            length = math.sqrt(dist_sq)
            rep[0] += (dx / length) * force
            rep[1] += (dy / length) * force
    rep_len = math.hypot(*rep)
    if rep_len > 1e-6:
        return (rep[0] / rep_len, rep[1] / rep_len)
    return None
```

### 6. 占领模式进度系统

```python
# 计算圈内双方人数
blue_in_zone = player_in_zone + teammates_in_zone
red_in_zone = enemies_in_zone

# 进度按人数差推进
capture_progress += (blue_in_zone - red_in_zone) * CAPTURE_RATE * dt

# 到达 30 秒获胜
if capture_progress >= CAPTURE_TIME:
    game_stats["won_games"] += 1
    game_stats["capture_wins"] += 1
    game_over(True)
```

### 7. 搜打撤容器与奖励

```python
# 容器奖励类型
REWARD_SCORE = 1    # 直接加分数
REWARD_FOOD  = 2    # 生成若干食物
REWARD_BOOST = 3    # 提供限时加速

def handle_container_collision(segment):
    for i, (cx, cy, cr, rt, rv) in enumerate(containers):
        if (segment[0]-cx)**2 + (segment[1]-cy)**2 < (cr + get_segment_radius())**2:
            del containers[i]
            if rt == REWARD_SCORE:
                score += rv
            elif rt == REWARD_FOOD:
                for _ in range(rv):
                    new_food = create_food(random.choice(FOOD_COLORS), FOOD_RADIUS)
                    if new_food:
                        foods.append(new_food)
            elif rt == REWARD_BOOST:
                temp_boost_remaining = rv
            return True
    return False
```

### 8. Windows 11 风格 UI

```python
MENU_HOVER = (230, 240, 255)        # 悬停浅蓝
MENU_HOVER_BORDER = (150, 190, 240) # 悬停边框
MENU_CHECK = (30, 100, 220)         # 选中标记

def draw_option_rect(surface, rect, text, font, is_selected=False, is_hovered=False):
    if is_hovered:
        draw_rounded_rect(screen, rect.inflate(10, 8), MENU_HOVER, radius=8)
        pygame.draw.rect(screen, MENU_HOVER_BORDER, rect.inflate(10, 8), 2, border_radius=8)
    elif is_selected:
        draw_rounded_rect(screen, rect.inflate(10, 8), MENU_HOVER, radius=8)
    # ...
```

- 圆角矩形（`border_radius`）
- 悬停浅蓝高亮
- 选中蓝勾标记
- 下拉菜单支持滚动（超过 5 项时）

### 9. 中文渲染兼容

```python
def get_font(size):
    scaled_size = int(size * SCALE)
    # 优先使用游戏目录下的微软雅黑字体文件
    local_font_path = os.path.join(os.path.dirname(__file__), "microsoft-yahei.ttf")
    if os.path.exists(local_font_path):
        try:
            return pygame.font.Font(local_font_path, scaled_size)
        except:
            pass
    # 回退到系统字体
    for name in ["Microsoft YaHei", "Microsoft YaHei UI", "SimHei", "SimSun", "KaiTi", "FangSong"]:
        try:
            font = pygame.font.SysFont(name, scaled_size)
            if font.render("测试", True, (255, 255, 255)).get_width() > 0:
                return font
        except:
            continue
    return pygame.font.Font(None, scaled_size)
```

### 10. 食物聚集算法

```python
def create_food(color, radius=FOOD_RADIUS):
    seg_radius = get_segment_radius()
    # 80% 概率沿用该颜色上次生成的中心点
    if color in color_centers and random.random() < 0.8:
        cx, cy = color_centers[color]
    else:
        cx, cy = random_position(margin=int(80 * SCALE) + 50)
    
    # 在中心点 ±80px 范围内尝试生成
    for _ in range(50):
        fx = cx + random.randint(-int(80 * SCALE), int(80 * SCALE))
        fy = cy + random.randint(-int(80 * SCALE), int(80 * SCALE))
        # 边界检查 + 重叠检查
        if not valid_position(fx, fy, radius): continue
        color_centers[color] = (fx, fy)
        return (fx, fy, color, radius)
    return None
```

同色食物聚集效果使地图上出现多个"食物带"，增加游戏策略性。

---

## 技术栈

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="48"/><br/>
<b>Python 3.8+</b><br/>
<sub>跨版本兼容</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pygame/pygame-original.svg" width="48"/><br/>
<b>Pygame</b><br/>
<sub>游戏引擎</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg" width="48"/><br/>
<b>pywin32</b><br/>
<sub>Named Pipe</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/json/json-original.svg" width="48"/><br/>
<b>JSON</b><br/>
<sub>存档与配置</sub>
</td>
</tr>
</table>

**Python 依赖**：

| 包名 | 版本 | 用途 |
|:-----|:----:|:-----|
| `pygame` | ≥ 2.0 | 游戏渲染与事件处理 |
| `pywin32` | ≥ 305 | Named Pipe IPC 通信 |
| `hashlib` | 内置 | HMAC-SHA256 签名 |
| `json` | 内置 | 成就 / 排行榜持久化 |
| `threading` | 内置 | IPC 后台线程 |

---

## 版本演进

### 从 Turtle 到 Pygame 的完整历程

| 版本 | 关键特性 | 引擎 |
|:-----|:---------|:----:|
| **1.0.0** | 基础玩法、鼠标控制、敌人 AI 觅食、Ctrl 加速 | Turtle |
| **2.1.0** | 摄像机跟随、大世界（3000×2000）、世界坐标系统 | Turtle |
| **2.10.0** | 自定义蛇头 / 蛇身颜色、方格背景、版本检测 | Turtle |
| **3.0.0** | Pygame 重写、60 FPS 流畅渲染、IPC 管道通信 | Pygame |
| **3.6.0** | 淘汰之王模式、排行榜功能 | Pygame |
| **3.10.0** | 淘汰之王升级至 100 名 AI | Pygame |
| **3.11.0** | AI 逻辑重写、绕前攻击、包抄策略 | Pygame |
| **3.27.0** | AI 10 种攻击策略、协同攻击 | Pygame |
| **4.0.0** | 搜打撤模式重做、三角洲行动风格、地图选择 | Pygame |
| **5.0.0** | 团队攻防 4v4、成就系统 | Pygame |
| **5.1.0** | 占领模式重做、AI 死亡重生 | Pygame |
| **5.2.0** | AI 追击优化、实时排名 | Pygame |
| **5.2.3** | HMAC 签名 IPC、修复 randint 崩溃 | Pygame |

### 架构演进图

```
v1.0.0 ──── Turtle 基础版
  │
  ├──▶ v2.1.0 ──── 摄像机 + 大世界
  │      │
  │      └──▶ v2.10.0 ──── 自定义颜色
  │             │
  │             └──▶ v3.0.0 ═══ Pygame 重写
  │                    │
  │                    ├──▶ v3.6.0 ──── 淘汰之王
  │                    ├──▶ v3.10.0 ─── 100 AI
  │                    ├──▶ v3.27.0 ─── AI 增强
  │                    ├──▶ v4.0.0 ──── 搜打撤
  │                    ├──▶ v5.0.0 ──── 团队 4v4 + 成就
  │                    └──▶ v5.2.3 ──── IPC + HMAC
```

---

## 文件说明

游戏运行时会在脚本所在目录生成以下文件：

| 文件 | 用途 |
|:-----|:-----|
| `player_name.txt` | 玩家名字（UTF-8 明文） |
| `timed_scores.json` | 淘汰之王排行榜（前 10 名） |
| `achievements.json` | 成就解锁状态 |
| `warehouse.json` | 搜打撤模式仓库物资（v4.0.0） |
| `microsoft-yahei.ttf` | 可选的中文字体文件 |

用户的 Windows 目录下：

| 文件 | 用途 |
|:-----|:-----|
| `~/.snake_version_pygame` | 版本号记录（用于更新日志提示） |
| `~/.snake_pve_version_pygame` | 旧版本号记录（v3.0.0 遗留） |

---

## 配套启动器

<table>
<tr>
<td align="center">
<a href="https://github.com/MMA131845/SnakeLauncherWPF">
<img src="https://img.shields.io/badge/SnakeLauncherWPF-v4.1.0-00b7c3?style=for-the-badge" />
</a>
<br/><br/>
<b>贪吃蛇启动器</b><br/>
<sub>WPF (.NET Framework 4.8) · Liquid Glass · IPC · 反作弊</sub>
</td>
</tr>
</table>

启动器通过 `SnakeGameFPSPipe` 管道接收游戏上报，实现：

- **实时状态栏** — FPS / 得分 / 击杀 / 模式 / 时长
- **数据统计页** — 累计游玩 / 启动次数 / 最高分
- **反作弊告警** — 签名失败 / 时间戳过期 / 增速异常
- **多版本管理** — 同时管理 C# 与 Python 版

### 游戏上报协议

```
FPS:60,SCORE:1200,KILLS:15,MODE:classic,TS:1735689600,SIG:a3f1b2c8...
```

| 字段 | 说明 |
|:-----|:-----|
| `FPS` | 当前实际帧率 |
| `SCORE` | 当前得分 |
| `KILLS` | 本局击杀数 |
| `MODE` | 游戏模式（`classic` / `timed` / `team4v4` / `mojin`） |
| `TS` | Unix 时间戳（秒） |
| `SIG` | HMAC-SHA256 签名（前 63 字符） |

启动器会校验时间戳窗口（±30 秒）与签名，防止重放攻击与数据篡改。

---

## 常见问题

<details>
<summary><b>Q1: 启动报错 "No module named 'win32pipe'"？</b></summary>

缺少 pywin32 库。安装方法：

```bash
pip install pywin32
```

安装后如仍报错，可能需要执行：

```bash
python Scripts/pywin32_postinstall.py -install
```
</details>

<details>
<summary><b>Q2: 中文显示为方块？</b></summary>

游戏优先使用以下字体：

1. 游戏目录下的 `microsoft-yahei.ttf`（可自行下载放入）
2. 系统字体：Microsoft YaHei / SimHei / SimSun / KaiTi / FangSong

如果全部缺失，会回退到 pygame 默认字体。**推荐**从 Windows 系统的 `C:\Windows\Fonts\msyh.ttc` 复制一份到游戏目录。
</details>

<details>
<summary><b>Q3: 游戏启动后闪退？</b></summary>

可能原因：

1. **Python 版本过低** — 需 3.8+
2. **Pygame 未安装** — 运行 `pip install pygame`
3. **杀毒软件拦截** — 加入白名单
4. **文件编码问题** — 确保使用 UTF-8 保存

从命令行运行查看错误信息：

```bash
python "贪吃蛇(5.2.3).py"
```
</details>

<details>
<summary><b>Q4: 如何切换游戏模式？</b></summary>

在主菜单按 `M` 键循环切换模式：

- 经典模式 → 淘汰之王 → 占领模式（4v4） → 经典模式
- 搜打撤模式需要在模式选择界面单独进入

点击模式文字或按 `M` 键均可切换。
</details>

<details>
<summary><b>Q5: 搜打撤模式怎么玩？</b></summary>

1. 从主菜单切换到搜打撤模式
2. 选择地图（废弃工厂 / 边境森林 / 航天基地）
3. 进入游戏后用鼠标控制移动
4. 靠近黄色容器按 `F` 搜索
5. 搜索完成后按 `F` 拾取奖励
6. 前往绿色撤离点，停留 9 秒撤离成功

**注意**：航天基地地图有红色燃烧弹危险区域。
</details>

<details>
<summary><b>Q6: 如何查看成就？</b></summary>

在主菜单按 `J` 键打开成就界面，包含 6 项成就：

- 初次击杀 — 第一次击杀敌人
- 十人斩 — 累计击杀 10 个敌人
- 五十人斩 — 累计击杀 50 个敌人
- 常胜将军 — 赢得 10 场游戏
- 生存专家 — 单局存活超过 5 分钟
- 占领专家 — 在占领模式中获胜
</details>

<details>
<summary><b>Q7: 排行榜不显示？</b></summary>

排行榜仅记录**淘汰之王模式**的得分。若从未在该模式得分，排行榜为空。每局结束且分数 > 0 时会自动保存到 `timed_scores.json`。
</details>

<details>
<summary><b>Q8: 如何调整游戏分辨率？</b></summary>

主菜单按 `S` → 「画面设置」 → 点击「画面分辨率」展开下拉菜单选择。支持 21 种分辨率，从 800×600 到 3840×2160。

切换分辨率后游戏会立即应用，所有 UI 元素会自动按比例缩放。
</details>

---

## 开发指南

### 添加新游戏模式

1. 定义模式标识符（如 `"battle"`）
2. 在主菜单的模式切换逻辑中添加
3. 在 `restart_game()` 中处理该模式的初始状态
4. 在 `draw()` 的游戏内渲染分支中添加专属绘制
5. 在主循环中添加该模式的更新逻辑
6. 参考 `get_enemy_new_direction()` 实现专属 AI

### 添加新成就

编辑 `ACHIEVEMENTS` 列表：

```python
ACHIEVEMENTS = [
    {"id": "new_achievement", "name": "新成就", "desc": "达成条件", "icon": "X"},
    # ...
]
```

然后在 `check_achievements()` 中添加检查逻辑：

```python
if condition and not achievements_unlocked.get("new_achievement", False):
    achievements_unlocked["new_achievement"] = True
    modified = True
```

### 添加新食物颜色

```python
FOOD_COLORS = [RED, ORANGE, YELLOW, PINK, PURPLE, CYAN, (0, 255, 0), 新颜色]
```

### 添加新背景样式

```python
BACKGROUND_STYLE_OPTIONS = ["纯黑", "纯白", "格子", "星空", "新样式"]
BACKGROUND_STYLE_VALUES = [BLACK, WHITE, "grid", "stars", "new_style"]

# 在 draw_background() 中处理新样式
```

---

## 开源协议

本项目基于 **MIT License** 开源，详见 [LICENSE](LICENSE)。

```
MIT License

Copyright (c) 2026 MEIMAOA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 致谢

<table>
<tr>
<td align="center" width="25%">
<b>开发</b><br/>
<sub>没冇啊</sub>
</td>
<td align="center" width="25%">
<b>代码协助</b><br/>
<sub>DeepSeek · ChatGPT<br/>Claude · Gemini</sub>
</td>
<td align="center" width="25%">
<b>美术设计</b><br/>
<sub>DeepSeek · 没冇啊</sub>
</td>
<td align="center" width="25%">
<b>QA 测试</b><br/>
<sub>没冇啊</sub>
</td>
</tr>
</table>

**特别感谢**：

- [Pygame](https://www.pygame.org/) 提供的开源游戏引擎
- [Python](https://www.python.org/) 编程语言
- [pywin32](https://github.com/mhammond/pywin32) 提供的 Windows API 封装
- 所有为这个项目点 Star、提 Issue、发 PR 的玩家与开发者

---

<div align="center">

### 如果这个项目对你有帮助，请点一个 Star

Made with love by **MEIMAOA**

*"Snake never dies, it just eats itself."*

[回到顶部](#snake-game-python-edition-)

</div>
