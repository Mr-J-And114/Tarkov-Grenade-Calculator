import math
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# Project Info
# ============================================================

APP_NAME = "Tarkov Grenade Calculator"
AUTHOR_NAME = "Mr.J.And"
GITHUB_REPOSITORY = "Mr-J-And114/Tarkov-Grenade-Calculator"
MAP_URL = "https://tarkov.dev/maps/"


# ============================================================
# Default AGS Parameters
# ============================================================

G = 9.81

DEFAULT_CALIBRATION_DISTANCE = 300.0
DEFAULT_CALIBRATION_ANGLE_DEG = 2.5

DEFAULT_VELOCITY = math.sqrt(
    DEFAULT_CALIBRATION_DISTANCE * G /
    math.sin(math.radians(DEFAULT_CALIBRATION_ANGLE_DEG * 2.0))
)


# ============================================================
# Language Data
# ============================================================

LANG = {
    "zh": {
        "window_title": "塔科夫榴弹射击辅助",
        "language": "语言",
        "current_velocity": "当前初速",
        "default_ags": "默认 AGS",
        "calibration": "校准点",
        "set_velocity": "设置初速",
        "restore_default": "恢复默认",
        "manual": "说明书",
        "open_map": "打开地图",

        "tab_mode1": "模式1：距离与高低差",
        "tab_mode2": "模式2：坐标计算",
        "tab_mode3": "模式3：射表",

        "input": "输入",
        "result": "结果",
        "calculate": "计算",
        "generate": "生成射表",

        "mode1_title": "根据水平距离和高低差计算俯仰角。",
        "height_rule_short": "高低差 = 目标高度 - 炮位高度；正数表示目标更高，负数表示目标更低。",
        "horizontal_distance": "水平距离 m",
        "height_difference": "高低差 m",

        "mode2_title": "根据炮位和目标坐标计算距离、方位角与俯仰角。",
        "launcher_x": "炮位 X",
        "launcher_y": "炮位 Y",
        "launcher_z": "炮位高度 Z",
        "target_x": "目标 X",
        "target_y": "目标 Y",
        "target_z": "目标高度 Z",
        "unknown_z_hint": "未知高度可填 0",
        "real_direction": "目标相对炮位的真实方位",
        "azimuth_rule": "方位角：北=0°，东=90°，南=180°，西=270°",

        "mode3_title": "生成 0~1000 米水平面射表。若存在高低差，请使用模式1或模式2。",
        "step": "步进 m",

        "north": "北",
        "north_east": "东北",
        "east": "东",
        "south_east": "东南",
        "south": "南",
        "south_west": "西南",
        "west": "西",
        "north_west": "西北",

        "input_error": "输入错误",
        "must_number": "必须输入数字。",
        "must_positive": "必须大于 0。",
        "success": "设置成功",
        "restored": "已恢复默认",

        "low_arc": "低弹道俯仰角",
        "high_arc": "高弹道参考角",
        "impossible": "无法命中",
        "possible_reason": "可能原因：距离过远、目标过高，或当前初速过低。",
        "azimuth": "方位角",
        "distance": "水平距离",
        "raw_delta": "原始坐标差",
        "corrected_east": "修正后东向分量",
        "corrected_north": "修正后北向分量",

        "velocity_window_title": "设置炮弹初速",
        "new_velocity": "新的炮弹初速 m/s",
        "temporary_velocity_hint": "该设置仅在本次运行期间有效，关闭软件后不会保存。",
        "apply": "应用",

        "table_header": "AGS 水平面射表",
        "same_height_condition": "条件：目标和炮位处于同一水平面，高低差 = 0。",

        "manual_title": "说明书",
    },

    "en": {
        "window_title": "Tarkov Grenade Calculator",
        "language": "Language",
        "current_velocity": "Current Velocity",
        "default_ags": "Default AGS",
        "calibration": "Calibration",
        "set_velocity": "Set Velocity",
        "restore_default": "Restore",
        "manual": "Manual",
        "open_map": "Open Map",

        "tab_mode1": "Mode 1: Distance + Height",
        "tab_mode2": "Mode 2: Coordinates",
        "tab_mode3": "Mode 3: Firing Table",

        "input": "Input",
        "result": "Result",
        "calculate": "Calculate",
        "generate": "Generate Table",

        "mode1_title": "Calculate elevation by horizontal distance and height difference.",
        "height_rule_short": "Height difference = target height - launcher height. Positive means higher, negative means lower.",
        "horizontal_distance": "Horizontal Distance m",
        "height_difference": "Height Difference m",

        "mode2_title": "Calculate distance, azimuth and elevation by launcher and target coordinates.",
        "launcher_x": "Launcher X",
        "launcher_y": "Launcher Y",
        "launcher_z": "Launcher Height Z",
        "target_x": "Target X",
        "target_y": "Target Y",
        "target_z": "Target Height Z",
        "unknown_z_hint": "Use 0 if unknown",
        "real_direction": "Real direction of target relative to launcher",
        "azimuth_rule": "Azimuth: North=0°, East=90°, South=180°, West=270°",

        "mode3_title": "Generate a 0-1000m horizontal firing table. Use Mode 1 or Mode 2 if height difference exists.",
        "step": "Step m",

        "north": "North",
        "north_east": "North-East",
        "east": "East",
        "south_east": "South-East",
        "south": "South",
        "south_west": "South-West",
        "west": "West",
        "north_west": "North-West",

        "input_error": "Input Error",
        "must_number": "must be a number.",
        "must_positive": "must be greater than 0.",
        "success": "Success",
        "restored": "Restored",

        "low_arc": "Low-arc Elevation",
        "high_arc": "High-arc Reference",
        "impossible": "Impossible",
        "possible_reason": "Possible reason: too far, target too high, or velocity too low.",
        "azimuth": "Azimuth",
        "distance": "Horizontal Distance",
        "raw_delta": "Raw Coordinate Delta",
        "corrected_east": "Corrected East Component",
        "corrected_north": "Corrected North Component",

        "velocity_window_title": "Set Projectile Velocity",
        "new_velocity": "New Projectile Velocity m/s",
        "temporary_velocity_hint": "This setting is temporary and will not be saved after closing the software.",
        "apply": "Apply",

        "table_header": "AGS Horizontal Firing Table",
        "same_height_condition": "Condition: target and launcher are at the same height, height difference = 0.",

        "manual_title": "Manual",
    }
}


DIRECTION_KEYS = [
    "north",
    "north_east",
    "east",
    "south_east",
    "south",
    "south_west",
    "west",
    "north_west",
]


DIRECTION_SIGNS = {
    "north": (0, 1),
    "north_east": (1, 1),
    "east": (1, 0),
    "south_east": (1, -1),
    "south": (0, -1),
    "south_west": (-1, -1),
    "west": (-1, 0),
    "north_west": (-1, 1),
}


# ============================================================
# Calculation Functions
# ============================================================

def calc_low_arc_angle(distance: float, height_diff: float, velocity: float):
    x = distance
    h = height_diff
    v = velocity
    g = G

    if x <= 0 or v <= 0:
        return None

    discriminant = v ** 4 - g * (g * x ** 2 + 2 * h * v ** 2)

    if discriminant < 0:
        return None

    sqrt_d = math.sqrt(discriminant)
    tan_theta_low = (v ** 2 - sqrt_d) / (g * x)
    theta_rad = math.atan(tan_theta_low)

    return math.degrees(theta_rad)


def calc_high_arc_angle(distance: float, height_diff: float, velocity: float):
    x = distance
    h = height_diff
    v = velocity
    g = G

    if x <= 0 or v <= 0:
        return None

    discriminant = v ** 4 - g * (g * x ** 2 + 2 * h * v ** 2)

    if discriminant < 0:
        return None

    sqrt_d = math.sqrt(discriminant)
    tan_theta_high = (v ** 2 + sqrt_d) / (g * x)
    theta_rad = math.atan(tan_theta_high)

    return math.degrees(theta_rad)


def calc_distance_2d(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)


def calc_azimuth_from_east_north(east, north):
    angle_rad = math.atan2(east, north)
    angle_deg = math.degrees(angle_rad)

    if angle_deg < 0:
        angle_deg += 360.0

    return angle_deg


def parse_float(value: str, field_name: str, lang: str):
    try:
        return float(value.strip())
    except Exception:
        raise ValueError(f"{field_name} {LANG[lang]['must_number']}")


def format_angle(angle):
    return f"{angle:.3f}°"


# ============================================================
# Main App
# ============================================================

class TarkovGrenadeCalculatorApp:
    def __init__(self, root):
        self.root = root

        self.lang = "zh"
        self.current_velocity = DEFAULT_VELOCITY

        self.m1_distance_var = tk.StringVar(value="300")
        self.m1_height_var = tk.StringVar(value="0")

        self.m2_x1_var = tk.StringVar(value="0")
        self.m2_y1_var = tk.StringVar(value="0")
        self.m2_z1_var = tk.StringVar(value="0")
        self.m2_x2_var = tk.StringVar(value="300")
        self.m2_y2_var = tk.StringVar(value="0")
        self.m2_z2_var = tk.StringVar(value="0")
        self.m2_direction_key = "east"

        self.m3_step_var = tk.StringVar(value="50")

        self.root.geometry("1060x720")
        self.root.minsize(960, 640)

        self.build_ui()

    def t(self, key):
        return LANG[self.lang][key]

    def build_ui(self):
        for child in self.root.winfo_children():
            child.destroy()

        self.root.title(f"{APP_NAME} - {self.t('window_title')}")

        self.create_top_bar()
        self.create_tabs()
        self.update_velocity_label()

    # ------------------------------------------------------------
    # Top Bar
    # ------------------------------------------------------------

    def create_top_bar(self):
        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, padx=10, pady=(8, 4))

        top.columnconfigure(0, weight=1)

        self.velocity_label = ttk.Label(top, text="", anchor="w")
        self.velocity_label.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        ttk.Label(top, text=self.t("language")).grid(row=0, column=1, padx=(4, 4))

        self.language_var = tk.StringVar(value="中文" if self.lang == "zh" else "English")
        language_box = ttk.Combobox(
            top,
            textvariable=self.language_var,
            values=["中文", "English"],
            state="readonly",
            width=9
        )
        language_box.grid(row=0, column=2, padx=4)
        language_box.bind("<<ComboboxSelected>>", self.on_language_changed)

        ttk.Button(top, text=self.t("set_velocity"), command=self.open_velocity_window, width=10).grid(row=0, column=3, padx=3)
        ttk.Button(top, text=self.t("restore_default"), command=self.restore_default_velocity, width=10).grid(row=0, column=4, padx=3)
        ttk.Button(top, text=self.t("manual"), command=self.open_manual_window, width=10).grid(row=0, column=5, padx=3)
        ttk.Button(top, text=self.t("open_map"), command=self.open_map_url, width=10).grid(row=0, column=6, padx=3)

    def on_language_changed(self, event=None):
        selected = self.language_var.get()
        self.lang = "zh" if selected == "中文" else "en"
        self.build_ui()

    def open_map_url(self):
        webbrowser.open(MAP_URL)

    def update_velocity_label(self):
        self.velocity_label.config(
            text=(
                f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s    "
                f"{self.t('default_ags')}: {DEFAULT_VELOCITY:.3f} m/s    "
                f"{self.t('calibration')}: 300m = 2.5°"
            )
        )

    # ------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=(4, 10))

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text=self.t("tab_mode1"))
        self.notebook.add(self.tab2, text=self.t("tab_mode2"))
        self.notebook.add(self.tab3, text=self.t("tab_mode3"))

        self.create_mode1()
        self.create_mode2()
        self.create_mode3()

    # ------------------------------------------------------------
    # Mode 1
    # ------------------------------------------------------------

    def create_mode1(self):
        frame = self.tab1
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)

        info = ttk.Label(
            frame,
            text=f"{self.t('mode1_title')}\n{self.t('height_rule_short')}",
            justify=tk.LEFT,
            wraplength=960
        )
        info.grid(row=0, column=0, sticky="ew", padx=14, pady=10)

        input_frame = ttk.LabelFrame(frame, text=self.t("input"))
        input_frame.grid(row=1, column=0, sticky="ew", padx=14, pady=8)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)

        ttk.Label(input_frame, text=self.t("horizontal_distance")).grid(row=0, column=0, sticky="e", padx=8, pady=10)
        ttk.Entry(input_frame, textvariable=self.m1_distance_var, width=16).grid(row=0, column=1, sticky="w", padx=8, pady=10)

        ttk.Label(input_frame, text=self.t("height_difference")).grid(row=0, column=2, sticky="e", padx=8, pady=10)
        ttk.Entry(input_frame, textvariable=self.m1_height_var, width=16).grid(row=0, column=3, sticky="w", padx=8, pady=10)

        ttk.Button(input_frame, text=self.t("calculate"), command=self.calculate_mode1, width=14).grid(
            row=0, column=4, sticky="e", padx=8, pady=10
        )

        result_frame = ttk.LabelFrame(frame, text=self.t("result"))
        result_frame.grid(row=2, column=0, sticky="nsew", padx=14, pady=8)
        result_frame.rowconfigure(0, weight=1)
        result_frame.columnconfigure(0, weight=1)

        self.m1_result_text = tk.Text(result_frame, wrap=tk.WORD, height=12)
        self.m1_result_text.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)

        scroll = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.m1_result_text.yview)
        scroll.grid(row=0, column=1, sticky="ns", padx=(0, 8), pady=8)
        self.m1_result_text.configure(yscrollcommand=scroll.set)

    def calculate_mode1(self):
        try:
            distance = parse_float(self.m1_distance_var.get(), self.t("horizontal_distance"), self.lang)
            height_diff = parse_float(self.m1_height_var.get(), self.t("height_difference"), self.lang)
        except ValueError as e:
            messagebox.showerror(self.t("input_error"), str(e))
            return

        low_angle = calc_low_arc_angle(distance, height_diff, self.current_velocity)
        high_angle = calc_high_arc_angle(distance, height_diff, self.current_velocity)

        lines = [
            f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s",
            f"{self.t('distance')}: {distance:.3f} m",
            f"{self.t('height_difference')}: {height_diff:.3f} m",
            "",
            self.t("height_rule_short"),
            "",
        ]

        if low_angle is None:
            lines.append(f"{self.t('low_arc')}: {self.t('impossible')}")
            lines.append(self.t("possible_reason"))
        else:
            lines.append(f"{self.t('low_arc')}: {format_angle(low_angle)}")

        if high_angle is None:
            lines.append(f"{self.t('high_arc')}: {self.t('impossible')}")
        else:
            lines.append(f"{self.t('high_arc')}: {format_angle(high_angle)}")

        self.set_text(self.m1_result_text, "\n".join(lines))

    # ------------------------------------------------------------
    # Mode 2
    # ------------------------------------------------------------

    def create_mode2(self):
        frame = self.tab2
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)

        info = ttk.Label(
            frame,
            text=f"{self.t('mode2_title')}\n{self.t('height_rule_short')}\n{self.t('azimuth_rule')}",
            justify=tk.LEFT,
            wraplength=960
        )
        info.grid(row=0, column=0, sticky="ew", padx=14, pady=10)

        input_frame = ttk.LabelFrame(frame, text=self.t("input"))
        input_frame.grid(row=1, column=0, sticky="ew", padx=14, pady=8)

        for i in range(6):
            input_frame.columnconfigure(i, weight=1)

        self.add_labeled_entry(input_frame, self.t("launcher_x"), self.m2_x1_var, 0, 0)
        self.add_labeled_entry(input_frame, self.t("launcher_y"), self.m2_y1_var, 0, 2)
        self.add_labeled_entry(input_frame, self.t("launcher_z"), self.m2_z1_var, 0, 4)

        self.add_labeled_entry(input_frame, self.t("target_x"), self.m2_x2_var, 1, 0)
        self.add_labeled_entry(input_frame, self.t("target_y"), self.m2_y2_var, 1, 2)
        self.add_labeled_entry(input_frame, self.t("target_z"), self.m2_z2_var, 1, 4)

        ttk.Label(input_frame, text=self.t("real_direction")).grid(row=2, column=0, sticky="e", padx=8, pady=10)

        direction_values = [self.t(k) for k in DIRECTION_KEYS]
        self.direction_display_var = tk.StringVar(value=self.t(self.m2_direction_key))

        direction_box = ttk.Combobox(
            input_frame,
            textvariable=self.direction_display_var,
            values=direction_values,
            state="readonly",
            width=18
        )
        direction_box.grid(row=2, column=1, sticky="w", padx=8, pady=10)
        direction_box.bind("<<ComboboxSelected>>", self.on_direction_changed)

        ttk.Button(input_frame, text=self.t("calculate"), command=self.calculate_mode2, width=14).grid(
            row=2, column=4, sticky="e", padx=8, pady=10
        )

        result_frame = ttk.LabelFrame(frame, text=self.t("result"))
        result_frame.grid(row=2, column=0, sticky="nsew", padx=14, pady=8)
        result_frame.rowconfigure(0, weight=1)
        result_frame.columnconfigure(0, weight=1)

        self.m2_result_text = tk.Text(result_frame, wrap=tk.WORD, height=12)
        self.m2_result_text.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)

        scroll = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.m2_result_text.yview)
        scroll.grid(row=0, column=1, sticky="ns", padx=(0, 8), pady=8)
        self.m2_result_text.configure(yscrollcommand=scroll.set)

    def add_labeled_entry(self, parent, label_text, variable, row, column):
        ttk.Label(parent, text=label_text).grid(row=row, column=column, sticky="e", padx=8, pady=8)
        ttk.Entry(parent, textvariable=variable, width=14).grid(row=row, column=column + 1, sticky="w", padx=8, pady=8)

    def on_direction_changed(self, event=None):
        selected_display = self.direction_display_var.get()

        for key in DIRECTION_KEYS:
            if self.t(key) == selected_display:
                self.m2_direction_key = key
                break

    def calculate_mode2(self):
        try:
            x1 = parse_float(self.m2_x1_var.get(), self.t("launcher_x"), self.lang)
            y1 = parse_float(self.m2_y1_var.get(), self.t("launcher_y"), self.lang)
            z1 = parse_float(self.m2_z1_var.get(), self.t("launcher_z"), self.lang)
            x2 = parse_float(self.m2_x2_var.get(), self.t("target_x"), self.lang)
            y2 = parse_float(self.m2_y2_var.get(), self.t("target_y"), self.lang)
            z2 = parse_float(self.m2_z2_var.get(), self.t("target_z"), self.lang)
        except ValueError as e:
            messagebox.showerror(self.t("input_error"), str(e))
            return

        dx = x2 - x1
        dy = y2 - y1

        distance = calc_distance_2d(x1, y1, x2, y2)
        height_diff = z2 - z1

        sign_east, sign_north = DIRECTION_SIGNS[self.m2_direction_key]

        east = sign_east * abs(dx) if sign_east != 0 else 0.0
        north = sign_north * abs(dy) if sign_north != 0 else 0.0

        azimuth = calc_azimuth_from_east_north(east, north)

        low_angle = calc_low_arc_angle(distance, height_diff, self.current_velocity)
        high_angle = calc_high_arc_angle(distance, height_diff, self.current_velocity)

        lines = [
            f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s",
            "",
            f"{self.t('launcher_x')}, {self.t('launcher_y')}, {self.t('launcher_z')}: "
            f"({x1:.3f}, {y1:.3f}, {z1:.3f})",
            f"{self.t('target_x')}, {self.t('target_y')}, {self.t('target_z')}: "
            f"({x2:.3f}, {y2:.3f}, {z2:.3f})",
            "",
            f"{self.t('raw_delta')}: dx = {dx:.3f}, dy = {dy:.3f}",
            f"{self.t('distance')}: {distance:.3f} m",
            f"{self.t('height_difference')}: {height_diff:.3f} m",
            "",
            f"{self.t('real_direction')}: {self.t(self.m2_direction_key)}",
            f"{self.t('corrected_east')}: {east:.3f} m",
            f"{self.t('corrected_north')}: {north:.3f} m",
            f"{self.t('azimuth')}: {format_angle(azimuth)}",
            self.t("azimuth_rule"),
            "",
        ]

        if low_angle is None:
            lines.append(f"{self.t('low_arc')}: {self.t('impossible')}")
            lines.append(self.t("possible_reason"))
        else:
            lines.append(f"{self.t('low_arc')}: {format_angle(low_angle)}")

        if high_angle is None:
            lines.append(f"{self.t('high_arc')}: {self.t('impossible')}")
        else:
            lines.append(f"{self.t('high_arc')}: {format_angle(high_angle)}")

        self.set_text(self.m2_result_text, "\n".join(lines))

    # ------------------------------------------------------------
    # Mode 3
    # ------------------------------------------------------------

    def create_mode3(self):
        frame = self.tab3
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)

        info = ttk.Label(
            frame,
            text=self.t("mode3_title"),
            justify=tk.LEFT,
            wraplength=960
        )
        info.grid(row=0, column=0, sticky="ew", padx=14, pady=10)

        input_frame = ttk.LabelFrame(frame, text=self.t("input"))
        input_frame.grid(row=1, column=0, sticky="ew", padx=14, pady=8)
        input_frame.columnconfigure(3, weight=1)

        ttk.Label(input_frame, text=self.t("step")).grid(row=0, column=0, sticky="e", padx=8, pady=10)
        ttk.Entry(input_frame, textvariable=self.m3_step_var, width=14).grid(row=0, column=1, sticky="w", padx=8, pady=10)

        ttk.Button(input_frame, text=self.t("generate"), command=self.generate_table, width=14).grid(
            row=0, column=2, sticky="w", padx=8, pady=10
        )

        result_frame = ttk.LabelFrame(frame, text=self.t("tab_mode3"))
        result_frame.grid(row=2, column=0, sticky="nsew", padx=14, pady=8)
        result_frame.rowconfigure(0, weight=1)
        result_frame.columnconfigure(0, weight=1)

        self.table_text = tk.Text(result_frame, wrap=tk.NONE)
        self.table_text.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)

        scroll_y = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.table_text.yview)
        scroll_y.grid(row=0, column=1, sticky="ns", padx=(0, 8), pady=8)

        scroll_x = ttk.Scrollbar(result_frame, orient=tk.HORIZONTAL, command=self.table_text.xview)
        scroll_x.grid(row=1, column=0, sticky="ew", padx=(8, 0), pady=(0, 8))

        self.table_text.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.generate_table()

    def generate_table(self):
        try:
            step = int(float(self.m3_step_var.get().strip()))
        except Exception:
            messagebox.showerror(self.t("input_error"), f"{self.t('step')} {self.t('must_number')}")
            return

        if step <= 0:
            messagebox.showerror(self.t("input_error"), f"{self.t('step')} {self.t('must_positive')}")
            return

        lines = [
            self.t("table_header"),
            f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s",
            self.t("same_height_condition"),
            "",
            f"{self.t('distance'):>12} | {self.t('low_arc'):>18} | {self.t('high_arc'):>18}",
            "-" * 60,
        ]

        distance = 0

        while distance <= 1000:
            if distance == 0:
                low_str = "0.000°"
                high_str = "-"
            else:
                low_angle = calc_low_arc_angle(distance, 0.0, self.current_velocity)
                high_angle = calc_high_arc_angle(distance, 0.0, self.current_velocity)

                low_str = self.t("impossible") if low_angle is None else f"{low_angle:.3f}°"
                high_str = self.t("impossible") if high_angle is None else f"{high_angle:.3f}°"

            lines.append(f"{distance:12d} | {low_str:>18} | {high_str:>18}")
            distance += step

        if hasattr(self, "table_text"):
            self.set_text(self.table_text, "\n".join(lines))

    # ------------------------------------------------------------
    # Velocity
    # ------------------------------------------------------------

    def open_velocity_window(self):
        win = tk.Toplevel(self.root)
        win.title(self.t("velocity_window_title"))
        win.geometry("420x220")
        win.resizable(False, False)

        ttk.Label(
            win,
            text=(
                f"{self.t('default_ags')}: {DEFAULT_VELOCITY:.3f} m/s\n"
                f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s\n\n"
                f"{self.t('temporary_velocity_hint')}"
            ),
            justify=tk.LEFT,
            wraplength=380
        ).pack(anchor="w", padx=16, pady=14)

        input_frame = ttk.Frame(win)
        input_frame.pack(fill=tk.X, padx=16, pady=8)

        ttk.Label(input_frame, text=self.t("new_velocity")).pack(side=tk.LEFT)

        velocity_var = tk.StringVar(value=f"{self.current_velocity:.3f}")
        ttk.Entry(input_frame, textvariable=velocity_var, width=14).pack(side=tk.LEFT, padx=8)

        def apply_velocity():
            try:
                new_v = parse_float(velocity_var.get(), self.t("new_velocity"), self.lang)
            except ValueError as e:
                messagebox.showerror(self.t("input_error"), str(e), parent=win)
                return

            if new_v <= 0:
                messagebox.showerror(
                    self.t("input_error"),
                    f"{self.t('new_velocity')} {self.t('must_positive')}",
                    parent=win
                )
                return

            self.current_velocity = new_v
            self.update_velocity_label()
            self.generate_table()
            messagebox.showinfo(
                self.t("success"),
                f"{self.t('current_velocity')}: {new_v:.3f} m/s",
                parent=win
            )
            win.destroy()

        ttk.Button(win, text=self.t("apply"), command=apply_velocity, width=12).pack(pady=12)

    def restore_default_velocity(self):
        self.current_velocity = DEFAULT_VELOCITY
        self.update_velocity_label()
        self.generate_table()
        messagebox.showinfo(
            self.t("restored"),
            f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s"
        )

    # ------------------------------------------------------------
    # Manual
    # ------------------------------------------------------------

    def open_manual_window(self):
        win = tk.Toplevel(self.root)
        win.title(self.t("manual_title"))
        win.geometry("760x620")
        win.minsize(680, 520)

        text = tk.Text(win, wrap=tk.WORD)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)

        scroll = ttk.Scrollbar(win, orient=tk.VERTICAL, command=text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

        text.configure(yscrollcommand=scroll.set)
        text.insert(tk.END, self.get_manual_text())
        text.configure(state=tk.DISABLED)

    def get_manual_text(self):
        if self.lang == "zh":
            return f"""
塔科夫榴弹射击辅助说明书
============================================================

作者：
    {AUTHOR_NAME}

GitHub 仓库：
    {GITHUB_REPOSITORY}

地图坐标来源：
    {MAP_URL}


一、用途
------------------------------------------------------------

本工具是用于《逃离塔科夫》的榴弹弹道辅助计算器，主要用于 AGS 榴弹发射器的距离、方位角和俯仰角计算。

本工具可以完成三类计算：

1. 根据水平距离和高低差计算俯仰角。
2. 根据炮位和目标坐标计算方位角与俯仰角。
3. 生成 0~1000 米的水平面射表。


二、默认 AGS 数据
------------------------------------------------------------

默认校准点：

    300m = 2.5°

程序使用重力加速度：

    g = 9.81 m/s²

根据校准点反推出默认等效初速：

    v = {DEFAULT_VELOCITY:.3f} m/s

注意：该初速是根据游戏内实测数据反推的等效值，不一定等于现实武器或游戏文件中的真实数值。


三、高低差规则
------------------------------------------------------------

高低差 = 目标高度 - 炮位高度。

正数表示目标比炮位高。
负数表示目标比炮位低。

例如：

    目标比炮位高 20 米，输入 20。
    目标比炮位低 35 米，输入 -35。


四、坐标模式
------------------------------------------------------------

坐标模式中：

    前者 = 炮位
    后者 = 目标

程序会根据两点坐标计算水平距离。

由于电子地图坐标轴可能与实际地图方向不完全一致，所以需要手动选择目标相对炮位的真实方位，例如东北、东南、西北等。

方位角定义：

    正北 = 0°
    正东 = 90°
    正南 = 180°
    正西 = 270°


五、射表模式
------------------------------------------------------------

射表模式会生成 0~1000 米水平面射表。

默认条件是：

    目标和炮位处于同一水平面。
    高低差 = 0。

如果存在高低差，请使用模式1或模式2计算，不要直接套用水平射表。


六、临时设置初速
------------------------------------------------------------

你可以通过“设置初速”临时修改炮弹飞行速度，以适配不同弹药或测试数据。

该设置不会保存，关闭程序后恢复默认。
也可以点击“恢复默认”手动恢复 AGS 默认数据。


七、地图链接
------------------------------------------------------------

本工具目前使用的坐标数据可以从 Tarkov.dev 地图获取：

    {MAP_URL}

点击主界面的“打开地图”即可跳转。


八、计算公式
------------------------------------------------------------

同水平面射程公式：

    R = v² / g * sin(2θ)

有高低差弹道方程：

    h = x * tan(θ) - g * x² / [2 * v² * cos²(θ)]

解出：

    tan(θ) = [v² ± sqrt(v⁴ - g(gx² + 2hv²))] / gx

低弹道使用减号。
高弹道使用加号。

实战中通常优先使用低弹道解。
"""
        else:
            return f"""
Tarkov Grenade Calculator Manual
============================================================

Author:
    {AUTHOR_NAME}

GitHub Repository:
    {GITHUB_REPOSITORY}

Map Coordinate Source:
    {MAP_URL}


1. Purpose
------------------------------------------------------------

This tool is a ballistic calculator for grenade launcher usage in Escape from Tarkov, mainly designed for AGS grenade launcher calculations.

It can:

1. Calculate elevation angle by horizontal distance and height difference.
2. Calculate azimuth and elevation by launcher and target coordinates.
3. Generate a 0-1000m horizontal firing table.


2. Default AGS Data
------------------------------------------------------------

Default calibration point:

    300m = 2.5°

Gravity:

    g = 9.81 m/s²

Default equivalent velocity calculated from the calibration point:

    v = {DEFAULT_VELOCITY:.3f} m/s

Note: this value is an equivalent velocity calculated from in-game measured data. It may not match real-world weapon data or internal game file data.


3. Height Difference Rule
------------------------------------------------------------

Height difference = target height - launcher height.

Positive means the target is higher.
Negative means the target is lower.

Examples:

    Target is 20 meters higher: input 20.
    Target is 35 meters lower: input -35.


4. Coordinate Mode
------------------------------------------------------------

In coordinate mode:

    First point = launcher.
    Second point = target.

The program calculates horizontal distance from the two coordinates.

Because some electronic map coordinate axes may not match real map directions, you need to manually select the real direction of the target relative to the launcher, such as North-East, South-East, or North-West.

Azimuth definition:

    North = 0°
    East = 90°
    South = 180°
    West = 270°


5. Firing Table Mode
------------------------------------------------------------

The firing table mode generates a 0-1000m horizontal firing table.

Default condition:

    Target and launcher are at the same height.
    Height difference = 0.

If height difference exists, use Mode 1 or Mode 2 instead of directly using the horizontal table.


6. Temporary Velocity Setting
------------------------------------------------------------

You can temporarily change projectile velocity through “Set Velocity”.

This can be used for other ammunition types or testing data.

The setting will not be saved after closing the program.
You can also click “Restore” to restore default AGS data.


7. Map Link
------------------------------------------------------------

Coordinate data can currently be obtained from Tarkov.dev maps:

    {MAP_URL}

Click “Open Map” in the main window to open it.


8. Formula
------------------------------------------------------------

Same-height range formula:

    R = v² / g * sin(2θ)

Trajectory equation with height difference:

    h = x * tan(θ) - g * x² / [2 * v² * cos²(θ)]

Solving for tan(θ):

    tan(θ) = [v² ± sqrt(v⁴ - g(gx² + 2hv²))] / gx

The low-arc solution uses the minus sign.
The high-arc solution uses the plus sign.

Usually the low-arc solution is recommended.
"""

    # ------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------

    @staticmethod
    def set_text(widget: tk.Text, content: str):
        widget.configure(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, content)
        widget.configure(state=tk.NORMAL)


# ============================================================
# Entry
# ============================================================

def main():
    root = tk.Tk()
    app = TarkovGrenadeCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()