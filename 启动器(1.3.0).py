import os
import re
import tempfile
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from threading import Thread
from functools import partial

# ---------- 游戏版本更新日志 ----------
GAME_CHANGELOGS = [
    ("v3.28.0", ["大幅提升淘汰之王模式难度：攻击阈值降低、速度4倍、绕前距离增加、预测时间延长、高分门槛降至15"]),
    ("v3.27.0", ["AI史诗级增强：躲避玩家身体优先级最高，10种攻击策略，有组织有预谋的协同攻击"]),
    ("v3.26.0", ["AI大幅度绕过蛇身，向蛇头前方攻击（扩大避障角度至±1.2弧度）"]),
    ("v3.25.0", ["名字输入改为独立界面，仅在首次启动时显示"]),
    ("v3.24.0", ["AI攻击速度从3倍改为2倍", "首次游戏需输入玩家名字", "淘汰之王模式实时显示所有敌人和玩家的排名列表（1-100）"]),
    ("v3.23.0", ["排名改为本局排名，实时显示玩家在当前对局中的名次"]),
    ("v3.22.0", ["AI攻击时智能避开其他蛇的身体，避免自杀式冲锋"]),
    ("v3.21.0", ["AI史诗级加强：战术角色分配（前锋/侧翼/后卫）、玩家轨迹预测、动态包围圈（仅淘汰之王模式）"]),
    ("v3.20.0", ["AI超级智能加强：预测玩家位置、动态绕前距离、智能分散包围、协同避免拥堵（仅淘汰之王模式）"]),
    ("v3.19.0", ["完全无解：只有分数≥20的敌人数量超过20个时，它们才会团结攻击玩家（仅淘汰之王模式）；否则保持躲避", "UI增加狂暴敌人计数器"]),
    ("v3.18.0", ["AI团结协作：多个AI会从左右两侧包抄玩家，形成包围（仅淘汰之王模式）"]),
    ("v3.17.0", ["AI攻击分数阈值从15改为20", "淘汰之王模式敌人生成随机名字", "被淘汰时显示淘汰者名字和最终排名", "排行榜改为保存所有分数，便于计算排名"]),
    ("v3.16.0", ["AI攻击绕前距离从5像素改为100像素"]),
    ("v3.15.0", ["AI攻击速度提升3倍，绕前距离缩短至5像素（仅淘汰之王模式）"]),
    ("v3.14.0", ["AI攻击加速：淘汰之王模式下分数≥15的AI移动速度提升1.5倍"]),
    ("v3.13.0", ["AI行为模式分离：淘汰之王模式下AI会加速移动到玩家前方攻击，经典模式沿用原逻辑（追击其他敌人）"]),
    ("v3.12.0", ["AI攻击方式改为绕到玩家前面，并且只攻击玩家"]),
    ("v3.11.0", ["AI逻辑重写：分数<15躲避所有人，分数≥15追击其他AI，吃食物优先级最低", "经典模式持续生成敌人，淘汰之王模式不补充", "默认蛇身颜色改为深绿"]),
    ("v3.10.2", ["排行榜优化：第一名显示“玩家”，其余显示“敌人”", "开始界面按钮悬停效果改为仅文字变灰"]),
    ("v3.10.1", ["优化排行榜显示格式：1. 玩家 (分数)"]),
    ("v3.10.0", ["淘汰之王模式敌人数量增至100"]),
    ("v3.9.0", ["淘汰之王模式移除时间限制，敌人数量增至43", "经典模式敌人数量增至10"]),
    ("v3.8.0", ["淘汰之王模式固定生成33名敌人"]),
    ("v3.7.0", ["淘汰之王模式改为固定敌人数量，敌人死亡后不再重生", "开局所有敌人同时生成，存活到时间结束即为胜利"]),
    ("v3.6.0", ["新增淘汰之王模式（限时生存，得分倍率递增）", "增加排行榜功能（仅限淘汰之王模式）"]),
    ("v3.5.0", ["AI会躲避玩家，优先级比吃食物高"]),
    ("v3.4.9", ["最低速度从0.5改回2"]),
    ("v3.4.8", ["修复分数始终为0的bug", "结算界面改为灰色半透明窗口"]),
    ("v3.4.7", ["添加结算界面，显示最终分数和操作选项", "游戏内UI颜色自适应背景（黑色背景白字，白色背景黑字）"]),
    ("v3.4.6", ["设置界面增加“开发者名单”选项，点击可查看制作人员"]),
    ("v3.4.5", ["修复玩家加速时敌人也加速的bug", "优化设置界面返回按钮：移除方框，仅保留文字"]),
    ("v3.4.4", ["设置界面左上角添加返回按钮，点击返回开始界面"]),
    ("v3.4.3", ["更新历史顺序改为最新到最老", "设置界面鼠标点击可直接更改选项值"]),
    ("v3.4.2", ["初始速度改为4.5，最低速度0.5", "设置界面支持鼠标悬停和点击（点击第四项直接打开更新日志）"]),
    ("v3.4.1", ["优化暂停菜单：鼠标悬停高亮，点击选择，键盘同时支持"]),
    ("v3.4.0", ["游戏内ESC打开暂停菜单（重新开始/返回开始界面/退出游戏）"]),
    ("v3.3.0", ["增加白色/浅灰交错方格背景", "设置中增加“更新日志”选项，可查看所有版本更新"]),
    ("v3.2.1", ["更新日志只在版本更新后首次启动显示"]),
    ("v3.2.0", ["更新日志改为单独窗口显示"]),
    ("v3.1.0", ["重做更新提示，游戏内直接显示", "修复开始界面按钮顺序错误", "修复中文无法显示的问题", "修复设置界面标题位置", "死亡提示加大加粗，颜色自适应", "优化性能，减少画面闪烁"]),
    ("v3.0.0", ["Pygame重写，流畅渲染", "支持鼠标/键盘控制", "敌人AI主动觅食", "敌人持续生成（最多10个）", "敌人死亡掉落红色大食物", "速度随分数递减", "Ctrl加速（5秒限时）", "蛇身随分数变粗", "敌人生成预警圆圈"]),
]

# ---------- 启动器更新日志 ----------
LAUNCHER_CHANGELOGS = [
    ("v1.0.0", ["初始版本，支持扫描和启动游戏文件"]),
    ("v1.1.0", ["添加手动选择文件功能", "修复文件名编码问题"]),
    ("v1.2.0", ["重新设计界面，采用左侧导航和卡片布局", "添加主题切换（浅色/深色）"]),
    ("v1.3.0", ["优化深色主题，提升可读性", "添加启动器更新日志"]),
    ("v1.3.1", ["修复：3.0.0以上版本只显示.bat文件，不显示.py文件"]),
    ("v1.4.0", ["启动器更新日志整合到设置页面内", "修复低版本无法启动的问题"]),
    ("v1.5.0", ["启动器更新日志和开发者名单改为独立页面"]),
]

# 制作人名单
CREDITS = [
    "开发者名单",
    "",
    "策划 & 开发：没冇啊",
    "代码：deep seek，没冇啊",
    "美术设计：deep seek，没冇啊",
    "QA：没冇啊",
    "",
    "特别感谢：所有支持本游戏的玩家",
    "",
    "Pygame 社区",
    "Python 编程语言",
]

# ---------- 主题定义 ----------
THEMES = {
    "light": {
        "name": "浅色",
        "bg": "#f5f5f5",
        "fg": "#333333",
        "menu_bg": "#2c3e50",
        "menu_fg": "#ecf0f1",
        "menu_hover_bg": "#34495e",
        "card_bg": "#ffffff",
        "card_fg": "#333333",
        "card_border": "#e0e0e0",
        "button_bg": "#0078d4",
        "button_fg": "white",
        "button_hover_bg": "#005a9e",
        "accent_button_bg": "#333333",
        "accent_button_fg": "white",
        "accent_button_hover_bg": "#555555",
        "list_bg": "white",
        "list_fg": "#333333",
        "list_select_bg": "#0078d4",
        "list_select_fg": "white",
        "text_bg": "white",
        "text_fg": "#333333",
    },
    "dark": {
        "name": "深色",
        "bg": "#0d1117",
        "fg": "#c9d1d9",
        "menu_bg": "#010409",
        "menu_fg": "#f0f6fc",
        "menu_hover_bg": "#1f2a3a",
        "card_bg": "#161b22",
        "card_fg": "#c9d1d9",
        "card_border": "#30363d",
        "button_bg": "#1f6feb",
        "button_fg": "white",
        "button_hover_bg": "#1158c7",
        "accent_button_bg": "#0078d4",
        "accent_button_fg": "white",
        "accent_button_hover_bg": "#005a9e",
        "list_bg": "#161b22",
        "list_fg": "#c9d1d9",
        "list_select_bg": "#1f6feb",
        "list_select_fg": "white",
        "text_bg": "#0d1117",
        "text_fg": "#c9d1d9",
    }
}

class ModernLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇版本启动器")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.current_theme = "light"
        self.theme = THEMES[self.current_theme]

        self.files = []          # (version_tuple, display_name, filepath, is_bat)
        self.card_frames = []    # 卡片Frame列表

        self.create_widgets()
        self.apply_theme()
        self.scan_files()

    def create_widgets(self):
        # 左侧导航栏
        self.nav_frame = tk.Frame(self.root, width=220)
        self.nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.nav_frame.pack_propagate(False)

        self.nav_title = tk.Label(self.nav_frame, text="贪吃蛇", font=("微软雅黑", 20, "bold"))
        self.nav_title.pack(pady=30)

        nav_buttons = [
            ("🏠 主页", "home"),
            ("📚 库", "library"),
            ("📋 启动器日志", "launcher_log"),
            ("👥 开发者", "credits"),
            ("⚙️ 设置", "settings")
        ]
        self.nav_btns = []
        for text, page in nav_buttons:
            btn = tk.Button(self.nav_frame, text=text, font=("微软雅黑", 12),
                            bd=0, anchor=tk.W, padx=20, pady=10,
                            command=lambda p=page: self.show_page(p))
            btn.pack(fill=tk.X, pady=2)
            self.nav_btns.append(btn)

        self.quit_btn = tk.Button(self.nav_frame, text="❌ 退出", font=("微软雅黑", 12),
                                   bd=0, anchor=tk.W, padx=20, pady=10,
                                   command=self.root.quit)
        self.quit_btn.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # 右侧主内容区域
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建页面
        self.pages = {}
        self.create_home_page()
        self.create_library_page()
        self.create_launcher_log_page()
        self.create_credits_page()
        self.create_settings_page()

        self.show_page("home")

    def create_home_page(self):
        frame = tk.Frame(self.content_frame)
        self.pages["home"] = frame

        welcome = tk.Label(frame, text="欢迎使用贪吃蛇版本启动器", font=("微软雅黑", 18, "bold"))
        welcome.pack(pady=20)

        log_title = tk.Label(frame, text="📜 游戏版本更新日志", font=("微软雅黑", 14, "bold"))
        log_title.pack(pady=10)

        text_frame = tk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(text_frame, yscrollcommand=scrollbar.set,
                                 font=("微软雅黑", 10), wrap=tk.WORD,
                                 borderwidth=0, highlightthickness=0)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)

        for ver, changes in GAME_CHANGELOGS:
            self.log_text.insert(tk.END, f"\n{ver}\n", "version")
            self.log_text.insert(tk.END, "-"*40 + "\n", "separator")
            for change in changes:
                self.log_text.insert(tk.END, f"  • {change}\n", "change")
        self.log_text.tag_config("version", font=("微软雅黑", 11, "bold"), foreground="#0078d4")
        self.log_text.tag_config("change", font=("微软雅黑", 10))
        self.log_text.config(state=tk.DISABLED)

    def create_library_page(self):
        frame = tk.Frame(self.content_frame)
        self.pages["library"] = frame

        toolbar = tk.Frame(frame)
        toolbar.pack(fill=tk.X, pady=10)

        tk.Label(toolbar, text="当前目录:", font=("微软雅黑", 10)).pack(side=tk.LEFT)
        self.path_label = tk.Label(toolbar, text=os.getcwd(), fg="blue", font=("微软雅黑", 10), cursor="hand2")
        self.path_label.pack(side=tk.LEFT, padx=5)
        self.path_label.bind("<Button-1>", self.copy_path)

        self.refresh_btn = tk.Button(toolbar, text="刷新", font=("微软雅黑", 10),
                                      bd=0, padx=15, pady=5, command=self.scan_files)
        self.refresh_btn.pack(side=tk.RIGHT, padx=5)

        self.manual_btn = tk.Button(toolbar, text="手动添加", font=("微软雅黑", 10),
                                     bd=0, padx=15, pady=5, command=self.manual_select)
        self.manual_btn.pack(side=tk.RIGHT, padx=5)

        canvas_frame = tk.Frame(frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.canvas = tk.Canvas(canvas_frame, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def create_launcher_log_page(self):
        frame = tk.Frame(self.content_frame)
        self.pages["launcher_log"] = frame

        title = tk.Label(frame, text="📋 启动器更新日志", font=("微软雅黑", 18, "bold"))
        title.pack(pady=20)

        text_frame = tk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.launcher_log_text = tk.Text(text_frame, yscrollcommand=scrollbar.set,
                                          font=("微软雅黑", 10), wrap=tk.WORD,
                                          borderwidth=0, highlightthickness=0)
        self.launcher_log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.launcher_log_text.yview)

        for ver, changes in LAUNCHER_CHANGELOGS:
            self.launcher_log_text.insert(tk.END, f"\n{ver}\n", "version")
            self.launcher_log_text.insert(tk.END, "-"*40 + "\n", "separator")
            for change in changes:
                self.launcher_log_text.insert(tk.END, f"  • {change}\n", "change")
        self.launcher_log_text.tag_config("version", font=("微软雅黑", 11, "bold"), foreground="#0078d4")
        self.launcher_log_text.tag_config("change", font=("微软雅黑", 10))
        self.launcher_log_text.config(state=tk.DISABLED)

    def create_credits_page(self):
        frame = tk.Frame(self.content_frame)
        self.pages["credits"] = frame

        title = tk.Label(frame, text="👥 开发者名单", font=("微软雅黑", 18, "bold"))
        title.pack(pady=20)

        canvas_frame = tk.Frame(frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        canvas = tk.Canvas(canvas_frame, highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for line in CREDITS:
            if line == "":
                tk.Label(scrollable_frame, text="", font=("微软雅黑", 11)).pack()
            elif "：" in line or ":" in line:
                parts = line.split("：") if "：" in line else line.split(":")
                if len(parts) == 2:
                    tk.Label(scrollable_frame, text=parts[0]+"：", font=("微软雅黑", 11, "bold")).pack(anchor=tk.W, pady=(5,0))
                    tk.Label(scrollable_frame, text=parts[1], font=("微软雅黑", 11)).pack(anchor=tk.W, padx=20)
                else:
                    tk.Label(scrollable_frame, text=line, font=("微软雅黑", 11, "bold")).pack(anchor=tk.W, pady=(5,0))
            else:
                tk.Label(scrollable_frame, text=line, font=("微软雅黑", 11)).pack(anchor=tk.W, padx=10)

    def create_settings_page(self):
        frame = tk.Frame(self.content_frame)
        self.pages["settings"] = frame

        title = tk.Label(frame, text="⚙️ 设置", font=("微软雅黑", 18, "bold"))
        title.pack(pady=20)

        theme_frame = tk.Frame(frame)
        theme_frame.pack(fill=tk.X, padx=50, pady=10)

        tk.Label(theme_frame, text="选择主题:", font=("微软雅黑", 12)).pack(side=tk.LEFT, padx=10)

        self.light_btn = tk.Button(theme_frame, text="浅色", font=("微软雅黑", 11),
                                    bd=0, padx=20, pady=5, command=lambda: self.set_theme("light"))
        self.light_btn.pack(side=tk.LEFT, padx=5)

        self.dark_btn = tk.Button(theme_frame, text="深色", font=("微软雅黑", 11),
                                   bd=0, padx=20, pady=5, command=lambda: self.set_theme("dark"))
        self.dark_btn.pack(side=tk.LEFT, padx=5)

    def show_page(self, page_name):
        for name, frame in self.pages.items():
            frame.pack_forget()
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)

    def set_theme(self, theme_name):
        self.current_theme = theme_name
        self.theme = THEMES[theme_name]
        self.apply_theme()

    def apply_theme(self):
        # 导航栏
        self.nav_frame.config(bg=self.theme["menu_bg"])
        self.nav_title.config(bg=self.theme["menu_bg"], fg=self.theme["menu_fg"])
        for btn in self.nav_btns:
            btn.config(bg=self.theme["menu_bg"], fg=self.theme["menu_fg"],
                       activebackground=self.theme["menu_hover_bg"],
                       activeforeground=self.theme["menu_fg"])
        self.quit_btn.config(bg=self.theme["menu_bg"], fg=self.theme["menu_fg"],
                             activebackground=self.theme["menu_hover_bg"],
                             activeforeground=self.theme["menu_fg"])

        # 内容区域
        self.content_frame.config(bg=self.theme["bg"])
        for page in self.pages.values():
            page.config(bg=self.theme["bg"])
            for child in page.winfo_children():
                if isinstance(child, tk.Frame):
                    child.config(bg=self.theme["bg"])
                    for sub in child.winfo_children():
                        if isinstance(sub, tk.Label):
                            sub.config(bg=self.theme["bg"], fg=self.theme["fg"])
                        elif isinstance(sub, tk.Button):
                            sub.config(bg=self.theme["button_bg"], fg=self.theme["button_fg"],
                                       activebackground=self.theme["button_hover_bg"],
                                       activeforeground=self.theme["button_fg"])
                        elif isinstance(sub, tk.Text):
                            sub.config(bg=self.theme["text_bg"], fg=self.theme["text_fg"])
                            # 更新文本标签颜色需要重新配置tag
                            try:
                                sub.tag_config("change", foreground=self.theme["fg"])
                            except:
                                pass

        # 库页面特殊控件
        if hasattr(self, 'path_label'):
            self.path_label.config(bg=self.theme["bg"])
        if hasattr(self, 'refresh_btn'):
            self.refresh_btn.config(bg=self.theme["button_bg"], fg=self.theme["button_fg"],
                                     activebackground=self.theme["button_hover_bg"])
        if hasattr(self, 'manual_btn'):
            self.manual_btn.config(bg=self.theme["button_bg"], fg=self.theme["button_fg"],
                                    activebackground=self.theme["button_hover_bg"])
        self.refresh_cards()

    def refresh_cards(self):
        for frame in self.card_frames:
            frame.destroy()
        self.card_frames.clear()

        if not self.files:
            label = tk.Label(self.scrollable_frame, text="未找到任何版本文件，请点击“手动添加”",
                             font=("微软雅黑", 12), bg=self.theme["bg"], fg=self.theme["fg"])
            label.pack(pady=20)
            self.card_frames.append(label)
            return

        self.files.sort(reverse=True, key=lambda x: x[0])
        cols = 3
        for i, (version_tuple, display_name, filepath, is_bat) in enumerate(self.files):
            row = i // cols
            col = i % cols

            card = tk.Frame(self.scrollable_frame, bg=self.theme["card_bg"],
                            relief=tk.FLAT, bd=1, highlightbackground=self.theme["card_border"],
                            highlightthickness=1)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            version_str = f"{version_tuple[0]}.{version_tuple[1]}.{version_tuple[2]}"
            if version_tuple == (0,0,0):
                version_str = "手动添加"
            ver_label = tk.Label(card, text=version_str, font=("微软雅黑", 12, "bold"),
                                 bg=self.theme["card_bg"], fg=self.theme["card_fg"])
            ver_label.pack(pady=(10,5))

            filename = os.path.basename(filepath)
            if len(filename) > 20:
                filename = filename[:17] + "..."
            name_label = tk.Label(card, text=filename, font=("微软雅黑", 10),
                                   bg=self.theme["card_bg"], fg=self.theme["card_fg"])
            name_label.pack(pady=5)

            btn = tk.Button(card, text="启动", font=("微软雅黑", 10, "bold"),
                            bg=self.theme["accent_button_bg"], fg=self.theme["accent_button_fg"],
                            activebackground=self.theme["accent_button_hover_bg"],
                            activeforeground=self.theme["accent_button_fg"],
                            bd=0, padx=15, pady=5,
                            command=partial(self.launch_file, filepath, is_bat))
            btn.pack(pady=10)

            self.card_frames.append(card)

        for r in range(row+1):
            self.scrollable_frame.grid_rowconfigure(r, weight=1)
        for c in range(cols):
            self.scrollable_frame.grid_columnconfigure(c, weight=1)

    def launch_file(self, filepath, is_bat):
        def run():
            try:
                if is_bat:
                    os.startfile(filepath)
                else:
                    temp_dir = tempfile.gettempdir()
                    safe_name = re.sub(r'[^\w\-_\. ]', '_', os.path.basename(filepath)).replace('.py', '')
                    batch_name = f"snake_launcher_{safe_name}.bat"
                    batch_path = os.path.join(temp_dir, batch_name)
                    with open(batch_path, 'w', encoding='ansi') as f:
                        f.write('@echo off\n')
                        f.write('chcp 65001 >nul\n')
                        f.write(f'python "{filepath}"\n')
                        f.write('pause\n')
                    os.startfile(batch_path)
                self.root.after(0, lambda: self.update_status("启动成功"))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("启动失败", f"文件: {filepath}\n错误: {str(e)}"))
                self.root.after(0, lambda: self.update_status("启动失败"))
        Thread(target=run, daemon=True).start()

    def scan_files(self):
        self.files = []
        pattern_py = re.compile(r'贪吃蛇[（(](\d+)\.(\d+)\.(\d+)[）)]\.py')
        pattern_bat = re.compile(r'贪吃蛇[（(](\d+)\.(\d+)\.(\d+)[）)]启动器\.bat')

        for filename in os.listdir('.'):
            match = pattern_py.match(filename)
            if match:
                major, minor, patch = map(int, match.groups())
                version_tuple = (major, minor, patch)
                # 版本 ≥ 3.0.0 的 .py 文件不显示（用户应使用对应的 .bat）
                if version_tuple >= (3,0,0):
                    continue
                self.files.append((version_tuple, filename, os.path.abspath(filename), False))
                continue
            match = pattern_bat.match(filename)
            if match:
                major, minor, patch = map(int, match.groups())
                version_tuple = (major, minor, patch)
                self.files.append((version_tuple, filename, os.path.abspath(filename), True))

        self.refresh_cards()
        self.update_status(f"找到 {len(self.files)} 个版本")

    def manual_select(self):
        file_path = filedialog.askopenfilename(
            title="选择游戏文件",
            filetypes=[("批处理文件", "*.bat"), ("Python文件", "*.py"), ("所有文件", "*.*")]
        )
        if not file_path:
            return
        file_path = os.path.abspath(file_path)
        base = os.path.basename(file_path)
        self.files.append(((0,0,0), base, file_path, file_path.lower().endswith('.bat')))
        self.refresh_cards()
        self.update_status(f"已添加手动文件: {base}")

    def copy_path(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(os.getcwd())
        self.update_status("目录路径已复制到剪贴板")

    def update_status(self, msg):
        self.root.title(f"贪吃蛇版本启动器 - {msg}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernLauncher(root)
    root.mainloop()