自由贪吃蛇 Python Edition
<div align="center">
https://img.shields.io/badge/version-1.0.0_to_5.2.3-brightgreen?style=for-the-badge
https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Pygame-2.x-00B140?style=for-the-badge&logo=python
https://img.shields.io/badge/Turtle-Builtin-3776AB?style=for-the-badge
https://img.shields.io/badge/license-MIT-blue?style=for-the-badge
https://img.shields.io/badge/platform-Windows-0078D4?style=for-the-badge&logo=windows

从 Turtle 到 Pygame，一款持续演进的现代贪吃蛇游戏

多版本合集 | 三种游戏模式 | 成就系统 | Named Pipe IPC | Win11 风格界面

项目简介 | 版本演进 | 核心玩法 | 快速开始 | 操作指南 | 技术亮点

</div>
项目简介
自由贪吃蛇 Python Edition 是一个整合了从 v1.0.0 到 v5.2.3 全部历史版本的仓库。它记录了一款贪吃蛇游戏从最朴素的 Turtle 实现，一步步演进为具备完整 PVE 系统、多元游戏模式、Win11 风格 UI 与现代 IPC 通信能力的成熟作品。

整个项目历时数十个版本的迭代，主要里程碑包括：

v1.0.0：Turtle 图形库版本，鼠标控制方向，敌人 AI 追踪食物

v3.0.0：全面重写为 Pygame 版本，游戏进入图形化时代

v3.6.0：新增「淘汰之王」模式，100 名 AI 同场竞技

v3.28.0：新增「搜打撤」摸金玩法

v4.0.0：搜打撤模式重做，图形设置界面完善

v5.0.0：新增「占领模式 4v4」团队对抗

v5.2.3：AI 行为与平衡性持续优化

核心特点：

三模式独立玩法：经典 / 淘汰之王 / 占领模式

完整 PVE 生态：敌人 AI 会追踪食物、包抄玩家、绕前拦截

现代 UI：Win11 风格下拉菜单、悬停高亮、滚动条、分辨率切换

存档加密：玩家名、成就、排行榜加密存储

IPC 通信：通过 Named Pipe 与 WPF 启动器实时同步状态

版本演进
版本分组
版本区间	技术栈	主要特征
1.0.0	Turtle	单文件简单实现，鼠标控制，敌人追踪食物
2.x.x	Turtle	引入加速、边界检测、聚集食物等基础系统
3.0.0 ~ 3.5.x	Pygame	引擎重写，UI 菜单化，鼠标控制统一
3.6.0 ~ 3.9.x	Pygame	淘汰之王模式，100 敌人同场竞技
3.10.0 ~ 3.36.1	Pygame	战术 AI、排行榜、障碍物、容器系统
4.0.0 ~ 4.0.3	Pygame	搜打撤重做，画面设置与帧率选项
5.0.0 ~ 5.2.3	Pygame	占领模式 4v4，团队 AI，IPC 通信
关键版本更新
<details> <summary>点击展开完整更新日志</summary>
v5.2.3

修复 random.randint 参数为浮点数的崩溃

进一步优化 AI 巡逻与攻击平衡

v5.2.2

修复团队模式敌方 AI 只追玩家的问题，现在会均衡攻击

敌方 AI 增加巡逻行为，速度微调，游戏更平衡

v5.2.1

敌方与友方 AI 增加绕前攻击，拦截蛇头移动

团队模式共享分数，队友击杀敌人玩家也得分

友方 AI 优化：有人占点时主动攻击 / 吃食物

v5.2.0

团队模式 AI 改进：敌方更积极追击玩家与队友

淘汰之王模式右上方显示实时排名

修复敌方 AI 无法攻击我方 AI 的问题

v5.1.0

团队 4v4 改为占领模式：占领中央据点 30 秒获胜

敌方 AI 死亡后会重生，保持持续压力

削弱友方 AI 攻击性，避免过强

平衡性调整，占领区域可视

v5.0.0

新增团队攻防 4v4 模式

v4.0.0

搜打撤模式重做

v3.28.0 ~ v3.36.1

摸金模式、三阶段战术 AI、容器系统

21 种分辨率、滚动条、下拉菜单美化

Win11 风格悬停反馈

v3.6.0 ~ v3.27.0

淘汰之王模式上线

AI 绕前攻击、包抄、预测位置

名字输入界面、本局排名显示

v3.0.0 ~ v3.5.0

Pygame 重写，ESC 暂停，加速修复

开发者名单、结算界面、最低速度限制

v1.0.0

首个公开版本，Turtle 实现

</details>
核心玩法
经典模式 (Classic)
最纯粹的贪吃蛇体验。

鼠标移动指向即为前进方向

食物数量：125（固定），蛇吃食物变长变粗

敌人数量：10 个，每 5 秒可能刷新一只

按 Ctrl 加速冲刺（5 秒上限，2 倍速）

撞敌人身体或世界边界即失败

敌人撞墙或撞自己身体会死亡并掉落红色大食物

淘汰之王 (Timed)
100 名 AI 同场竞技，实时排名。

100 名 AI + 你 = 101 人局

右上角显示实时排名（前 15 名）

AI 会追踪食物、攻击玩家、包抄绕前

玩家分数越高，移动速度越慢

游戏结束后分数计入历史排行榜

占领模式 (Team 4v4)
与 3 名友方 AI 合作，占领中央据点。

4v4 团队对抗，地图为 1000 x 800 缩小战场

玩家或友方 AI 站在中央圆圈内推进进度

占领满 30 秒即胜利

敌方 AI 被击杀后 3 秒原地重生

顶部显示占领进度条

友方 AI：有人占点时主动攻击 / 吃食物，无人占点时前往据点

敌人 AI 行为
敌人具备多层次决策能力：

追踪食物：80% 概率朝向最近食物移动

预测拦截：根据玩家速度与方向，预测 80px 后的位置并绕前

碰撞规避：使用排斥力场避开其他蛇身与障碍物

巡逻：无目标时围绕占领区随机游走

禁止反向：所有决策均不允许 180 度掉头

快速开始
环境要求
操作系统：Windows 10 / 11

Python：3.8 或更高版本

依赖库：

bash
pip install pygame pywin32
说明：pywin32 仅在 v5.x 的 IPC 功能中需要；turtle 为 Python 内置，无需安装。

运行游戏
选择想要体验的版本，直接运行对应的 .py 文件：

bash
# 体验最初版本（Turtle）
python "贪吃蛇(1.0.0).py"

# 体验最新版本（Pygame）
python "贪吃蛇(5.2.3).py"
打包为 EXE（可选）：

bash
pyinstaller --onefile --windowed "贪吃蛇(5.2.3).py"
首次启动
首次运行会弹出名字输入界面，输入你的昵称（最多 20 字符）

若检测到版本变化，会显示更新日志，按空格或点击「开始游戏」

进入主菜单后，按 M 键切换游戏模式

按 空格键开始游戏

操作指南
全局快捷键
按键	功能
鼠标移动	控制蛇头方向
Ctrl	加速冲刺（长按持续，5 秒上限）
Esc	暂停 / 返回上一级
空格	主菜单：开始游戏
S	主菜单：打开设置
Q	主菜单：退出游戏
M	主菜单：切换游戏模式
H	主菜单：查看历史排行榜
J	主菜单：查看成就
设置界面
按键	功能
上下方向键	选择设置项
左右方向键	更改当前项数值
Enter	保存并退出
Esc	取消更改并退出
可配置项：

背景样式：纯黑 / 纯白 / 格子 / 星空

蛇头颜色：浅绿 / 黄 / 橙 / 粉 / 青 / 白

蛇身颜色：绿 / 深绿 / 蓝 / 紫 / 棕 / 灰

画面设置：分辨率 / 显示模式 / 界面主题 / 最高帧数

查看更新日志

开发者名单

画面设置
选项	可选项
分辨率	21 种，从 800x600 到 3840x2160
显示方式	无边框全屏 / 窗口化（无边框）/ 窗口化
界面主题	白色 / 浅灰 / 浅蓝 / 浅绿 / 浅粉
最高帧数	30 / 60 / 120 / 144 / 240

技术亮点
1. 从 Turtle 到 Pygame 的架构跃迁
v1.0.0 使用 Python 内置 Turtle 库实现，单文件不到 500 行：

python
# v1.0.0：Turtle 实现片段
screen = turtle.Screen()
screen.title("自由贪吃蛇 (PVE)")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
screen.tracer(0)  # 关闭自动刷新，手动控制
v3.0.0 起全面切换到 Pygame，获得硬件加速、Sprite 系统、多点触控等能力：

python
# v5.2.3：Pygame 实现
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
clock = pygame.time.Clock()
好处在于：帧率稳定、渲染性能提升 10 倍以上、支持真正的全屏与分辨率切换。

2. 摄像机跟随的世界坐标系统
游戏世界固定为 5000 x 4000，摄像机实时跟随蛇头：

python
def update_camera(head_x, head_y):
    global cam_x, cam_y
    cam_x, cam_y = head_x, head_y
    min_cam_x = WORLD_MIN_X + SCREEN_WIDTH // 2
    max_cam_x = WORLD_MAX_X - SCREEN_WIDTH // 2
    if min_cam_x < max_cam_x:
        cam_x = max(min_cam_x, min(cam_x, max_cam_x))
    # ...
所有绘制都通过 world_to_screen() 转换，保证在不同分辨率下坐标一致：

python
def world_to_screen(wx, wy):
    return int(wx - cam_x + SCREEN_WIDTH // 2), int(wy - cam_y + SCREEN_HEIGHT // 2)
3. 自适应缩放系统
以 1600 x 900 为设计基准，所有尺寸在启动时按比例缩放：

python
BASE_WIDTH, BASE_HEIGHT = 1600, 900
SCALE_X = SCREEN_WIDTH / BASE_WIDTH
SCALE_Y = SCREEN_HEIGHT / BASE_HEIGHT
SCALE = min(SCALE_X, SCALE_Y)

BUTTON_WIDTH = int(300 * SCALE)
BUTTON_HEIGHT = int(44 * SCALE)
GRID_SIZE = int(40 * SCALE)
切换分辨率时通过 apply_display_settings() 一次性重算所有尺寸常量。

4. 颜色聚类食物生成
普通食物并非完全随机分布，而是按颜色聚集——同色食物倾向出现在上一次同色食物附近的 80 像素范围内：

python
def create_food(color, radius=FOOD_RADIUS):
    if color in color_centers and random.random() < 0.8:
        cx, cy = color_centers[color]
    else:
        cx, cy = random_position(margin=int(80 * SCALE) + 50)
    # 在中心点附近尝试 50 次生成
    # ...
这产生了「红区」「蓝区」的视觉效果，让地图更有层次。

5. 多层次 AI 决策
敌人 AI 每帧按照优先级依次尝试：

python
def get_enemy_new_direction(enemy, all_enemies):
    # 1. 若前方即将撞上，紧急避让（排斥力场）
    if will_collide_with_player(head, old_dir, radius):
        evade = get_evade_direction(head, hostile_segments, old_dir, radius)
        if evade: return evade

    # 2. 60% 概率追踪玩家（使用预测位置绕前）
    if random.random() < 0.6:
        pred_pos = intercept_position(player_head, direction, get_current_speed(), head)
        # ...

    # 3. 否则追踪队友
    # 4. 否则巡逻占领区
    # 5. 兜底：随机非反向方向
其中 intercept_position() 会预测目标 80 像素后的位置，让 AI 学会「绕前拦截」而非单纯追尾。

6. Named Pipe IPC 通信
v5.x 版本通过 Windows Named Pipe 与 WPF 启动器实时同步状态：

python
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
                line = f"FPS:{fps},SCORE:{score},KILLS:{kills},MODE:{mode_str}\n"
                win32file.WriteFile(handle, line.encode())
                time.sleep(0.5)
        except:
            pass
        time.sleep(2)
启动器接收后解析并在状态栏展示。断开后自动重连，对游戏本身零影响。

7. 成就系统
6 项成就覆盖不同玩法维度：

ID	名称	达成条件
first_kill	初次击杀	第一次击杀敌人
kill_10	十人斩	累计击杀 10 个敌人
kill_50	五十人斩	累计击杀 50 个敌人
win_10	常胜将军	赢得 10 场游戏
survival_5min	生存专家	单局存活超过 5 分钟
capture_win	占领专家	在占领模式中获胜
检测通过闭包方式避免重复触发：

python
def check_achievements():
    global achievements_unlocked
    modified = False
    if game_stats["total_kills"] >= 1 and not achievements_unlocked.get("first_kill"):
        achievements_unlocked["first_kill"] = True
        modified = True
    # ...
    if modified:
        save_achievements(achievements_unlocked)
8. 字体多级回退
为保证中文在所有 Windows 机器上正确显示，实现字体回退链：

python
def get_font(size):
    # 1. 尝试加载项目目录下的微软雅黑字体文件
    local_font_path = os.path.join(os.path.dirname(__file__), "microsoft-yahei.ttf")
    if os.path.exists(local_font_path):
        try: return pygame.font.Font(local_font_path, scaled_size)
        except: pass
    # 2. 尝试系统字体链
    for name in ["Microsoft YaHei", "Microsoft YaHei UI", "SimHei", "SimSun", "KaiTi", "FangSong"]:
        try:
            font = pygame.font.SysFont(name, scaled_size)
            if font.render("测试", True, (255,255,255)).get_width() > 0:
                return font
        except: continue
    # 3. 兜底使用 pygame 内置字体
    return pygame.font.Font(None, scaled_size)
9. Win11 风格下拉菜单
支持滚动条、勾选标记、悬停高亮：

python
def draw_dropdown_menu(option_rect, items, current_index, menu_type):
    # ...
    # 当项目超过 5 个时启用滚动条
    if total_items > max_visible:
        thumb_height = max(20, scroll_bar_height * max_visible / total_items)
        thumb_y = scroll_bar_y + (scroll_offset / (total_items - max_visible)) * (
            scroll_bar_height - thumb_height)
        # 绘制滚动条与滑块
    # 当前选中项右侧显示勾选标记
    if actual_index == current_index:
        check_surf = get_font(24).render("✓", True, MENU_CHECK)
        screen.blit(check_surf, (item_rect.right - check_surf.get_width() - 15, ...))
10. 加密存档设计
玩家名、排行榜、成就数据均通过 SecureStorage 加密存储（启动器端实现，游戏端通过 IPC 间接使用），防止普通用户直接编辑存档。游戏内所有文件读写均通过统一的 load_xxx / save_xxx 函数封装，便于后续替换存储后端。

更新日志
v5.2.3（当前版本）
修复

修复 random.randint 参数为浮点数的崩溃

进一步优化 AI 巡逻与攻击平衡

v5.2.x 系列
AI 绕前攻击、拦截蛇头移动

团队模式共享分数，队友击杀玩家也得分

敌方 AI 均衡攻击队友与玩家

淘汰之王模式实时排名

v5.1.x 系列
占领模式替代团队 4v4

敌方 AI 死亡后重生

占领区域可视化

v5.0.x 系列
新增团队攻防 4v4

地图缩小为 800x600 提升战斗节奏

默认 30 FPS

v4.0.x 系列
搜打撤重做

画面设置新增最高帧数选项

修复移动穿透与下拉菜单错误

v3.x 系列
Pygame 重写

淘汰之王、摸金模式、三阶段战术 AI

21 种分辨率、Win11 风格界面

名字输入、排行榜、成就

v1.0.0
首个公开版本，Turtle 实现

贡献指南
欢迎提交 Issue 和 Pull Request。

bash
# Fork 后克隆
git clone https://github.com/MMA131845/Snake-Game-Python-Edition.git
cd Snake-Game-Python-Edition

# 创建功能分支
git checkout -b feature/amazing-feature

# 提交修改
git commit -m "feat: 添加新功能"

# 推送分支
git push origin feature/amazing-feature

# 在 GitHub 上打开 Pull Request
代码规范
使用 snake_case 命名函数与变量，UPPER_CASE 命名常量

新增游戏模式请保持 game_mode 字段的字符串标识风格

新增 UI 元素时优先使用 draw_rounded_rect 与 draw_option_rect 保持视觉统一

所有涉及缩放的尺寸必须乘以 SCALE

提交前请确认在 800x600 与 1920x1080 两种分辨率下均能正常运行

开源协议
本项目基于 MIT License 开源，详见 LICENSE 文件。

text
MIT License

Copyright (c) 2026 MEIMAOA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
致谢
开发：没冇啊

代码：DeepSeek、没冇啊

美术设计：DeepSeek、没冇啊

QA：没冇啊

特别感谢：所有支持本游戏的玩家

Pygame 社区与 Python 编程语言

<div align="center">
如果这个项目对你有帮助，欢迎点一个 Star

Made with love by MEIMAOA

https://visitor-badge.laobi.icu/badge?page_id=MMA131845.Snake-Game-Python-Edition

</div>
