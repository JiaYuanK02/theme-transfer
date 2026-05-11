# @Time    : 2025/10/29 20:38
# @Author  : KJY
# @version : 1.0
# @File    : test.py



import tkinter as tk
import threading
import random
import time
from datetime import datetime

def get_text_color(bg_hex):
    r = int(bg_hex[1:3], 16)
    g = int(bg_hex[3:5], 16)
    b = int(bg_hex[5:7], 16)
    brightness = (r*299 + g*587 + b*114)/1000
    return '#FFFFFF' if brightness < 128 else '#333333'

def get_period():
    hour = datetime.now().hour
    if 5 <= hour < 9: return "morning"
    elif 9 <= hour < 12: return "forenoon"
    elif 12 <= hour < 17: return "afternoon"
    elif 17 <= hour < 20: return "evening"
    elif 20 <= hour < 23: return "night"
    else: return "midnight"

def create_rounded_rect(canvas, x1, y1, x2, y2, radius=20, **kwargs):
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# 通用提示词
COMMON_TIPS = [
        "别忘了喝水哦 💧", "休息一下眼睛 👀", "抬头看看天空～",
        "你已经做得很好啦 🌼", "保持微笑，世界更可爱 😊",
        "偶尔发呆，也是生活的一部分 🌙", "记得多爱自己一点 💖",
        "你的快乐，比完美更重要", "偶尔摆烂，地球照转", "你值得一切美好",
        "你已经做得很好啦", "今天的心情是彩虹色", "你的存在，让世界多了一分可爱",
        "不必迎合所有人，你的特别自有磁场", "拒绝内耗，直接发疯(bushi)",
        "小小世界，开心至上", "你是生活钦定的主角", "休息不是偷懒，是充电",
        "你的情绪值得被重视", "把自己重新养一遍", "你可以脆弱，可以停下",
        "世界很吵， 但你只需听自己的心","一个人也要好好的",
        "要好好吃饭","要好好爱自己","身体健康","万事如意",
        "期待第一次见面","天冷了多穿衣服","梦想成真","要多喝水哦(●ˇ∀ˇ●)",
        "有些温柔在风里，也在你心里 💫","慢一点，生活不会跑掉 🌿",
        "你已经做得很好啦 🍀","风会记得你的笑 🌈","给自己一点掌声吧 👏"
    ]

# 最终居中提示
FINAL_MESSAGE = "漂亮女孩，明天给你来杯万里木兰，大杯，标准冰，七分糖，甜你一整天！🌹🌹🌹 \n\n我倒，不许拒绝哟！！！"

# 气泡显示函数
def show_rounded_bubble(tip_text, bg_color=None):
    window = tk.Tk()
    window.overrideredirect(True)
    window.attributes("-topmost", True)
    window.attributes("-alpha", 0.0)
    window.attributes("-transparentcolor", "white")

    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = 300, 100
    x = random.randint(0, max(0, sw - w))
    y = random.randint(0, max(0, sh - h))
    window.geometry(f"{w}x{h}+{x}+{y}")

    # 如果没有指定背景色，则随机选择
    bg_colors = [
        "#FFE4E1",  # mistyrose
        "#FFF0F5",  # lavenderblush
        "#F0F8FF",  # aliceblue
        "#F0FFF0",  # honeydew
        "#FFFACD",  # lemonchiffon
        "#FFF5EE",  # seashell
        "#FFDAB9",  # peachpuff
        "#E0FFFF",  # lightcyan
        "#F0FFFF",  # azure
        "#B0E0E6",  # powderblue
        "#AFEEEE",  # paleturquoise
        "#FFFFE0",  # lightyellow
        "#F5FFFA",  # mintcream
        "#FDF5E6",  # oldlace
        "#FFF8DC",  # cornsilk
        "#FFEFD5",  # papayawhip
        "#FFFAF0",  # floralwhite
        "#FAF0E6",  # linen
        "#D8BFD8",  # thistle
        "#FFB6C1",  # lightpink
        "#DDA0DD",  # plum
        "#F0E68C",  # khaki
        "#EEE8AA",  # palegoldenrod
        "#FFDEAD",  # navajowhite
        "#FFEBCD",  # blanchedalmond
        "#E6E6FA",  # lavender
        "#F5F5DC",  # beige
        "#F5DEB3",  # wheat
        "#DCDCDC",  # gainsboro
        "#FAEBD7",  # antiquewhite
        "#B0C4DE",  # lightsteelblue
        "#87CEEB",  # skyblue
        "#98FB98",  # palegreen
        "#7FFFD4",  # aquamarine
        "#FFE4C4",  # bisque
        "#BC8F8F",  # rosybrown
        "#FAFAD2",  # lightgoldenrodyellow
        "#FFC0CB",  # pink
        "#FFE4B5",  # moccasin
        "#F08080",  # lightcoral
        "#FFA07A",  # lightsalmon
        "#ADD8E6"  # lightblue
    ]

    if bg_color is None:
        bg_color = random.choice(bg_colors)

    fg = get_text_color(bg_color)

    canvas = tk.Canvas(window, width=w, height=h, highlightthickness=0, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)
    create_rounded_rect(canvas, 0, 0, w, h, radius=20, fill=bg_color, outline=bg_color)
    canvas.create_text(w/2, h/2, text=tip_text, font=("圆体", 16), fill=fg, width=w-40)

    def animate():
        # 淡入
        for i in range(21):
            window.attributes("-alpha", i / 20)
            time.sleep(0.05)
        # 浮动
        float_dir = 1
        for _ in range(60):
            y_new = window.winfo_y() + float_dir
            if y_new <= 0 or y_new + h >= sh: float_dir *= -1
            window.geometry(f"{w}x{h}+{x}+{y_new}")
            time.sleep(0.05)
        # 淡出
        for i in range(20, -1, -1):
            window.attributes("-alpha", i / 20)
            time.sleep(0.05)
        window.destroy()

    threading.Thread(target=animate, daemon=True).start()
    window.mainloop()

# 顺序显示所有提示词，包括时间段提示 + 通用提示 + 最终提示
def launch_all_bubbles():
    period = get_period()

    # 各时间段提示词（控制在50句左右）
    TIPS = {
        "morning": [
            "早安，新的希望在等你 🌅", "清风拂面，心情自然轻快～", "愿今天的阳光刚好，心情正妙 ☀️",
            "晨起露微霜，君笑暖心房。", "今日宜：拥抱生活💛", "一杯清茶，一份惬意，一天安好。",
            "朝霞映红天，也映你笑颜。", "今朝有梦，恰似初见。", "早安呀，小确幸在路上～",
            "你若安好，便是晴天 🌤️",
            "早安！新的一天从微笑开始☀️", "吃早餐了吗？空腹可不行～",
            "晨风带着希望，请你迎光前行。", "又是元气满满的一天！",
            "阳光照在脸上，也要照进心里🌤", "早晨的空气最甜，深呼吸一下！",
            "生活的温柔都在清晨的风里。", "别忘了带笑出门。",
            "去做喜欢的事，去成为更好的你！", "一杯清茶，一缕晨光，生活美好又明亮。",
            "愿你今天的每一步都轻盈而坚定。", "旭日初升，心怀热望，奔向未来！",
            "晨风轻拂，别忘了笑一笑。", "晨起闻花香，心情也芬芳。",
            "莫负朝阳与希望。", "人间朝气，如你笑意。",
            "努力是为了有选择的自由。", "今天也要比昨天更自信一点。",
            "晨曦微露，梦与光同行。", "太阳都起床啦，你也要闪闪发光。",
            "人生就像早晨的阳光，再多云也挡不住。", "新的一天，别让自己失望。",
            "温柔地开始，坚定地走下去。", "给生活一个笑脸，它会还你一个拥抱。",
            "每一个清晨，都是希望的重启键。", "今天也要相信自己是被喜欢的。",
            "喝杯热水，暖胃也暖心。", "世界会因为你起床而明亮一点✨",
            "你要相信，所有努力都算数。", "别怕路远，梦在终点等你。",
            "去迎接阳光吧，昨日的阴霾不重要了。", "今天的风都在夸你精神焕发～",
            "早晨的第一缕阳光，送给最努力的你。", "花未开全，梦未圆满，都别急。",
            "别忘了笑哦，你的笑会比阳光更暖。", "今天也要好好爱自己。",
            "清晨的咖啡香里藏着小确幸。", "你要做自己的光，不必等谁来照亮。",
            "希望你心里有光，眼中有光，笑容也有光。", "愿你被世界温柔以待，也愿你温柔待世界。",
            "天亮了，新故事要开始了。", "就算只是微小的一步，也是新的开始。",
            "早安，带上笑容去生活吧。", "心向光亮，步履不停。",
            "早安！新的一天开始啦 🌞", "早安，带上笑容去生活吧。", "心向光亮，步履不停。",
            "今天的风也在替我问候你。", "早起的鸟儿不一定有虫吃，但会更自由。",
            "希望今天的你，依旧闪光。", "把昨天的疲惫留在梦里吧。", "如果觉得累，就对自己温柔一点。",
            "你要相信，所有的好事都在路上。", "希望今天一切顺心如意～",
            "早晨好像一封温柔的信，寄给正在努力的你。", "今天也要比昨日更靠近梦想一点。",
            "万物都在发芽，你也要充满生机。", "早晨的风轻轻吹过，替我说声：想你。"
        ],

        "forenoon": [
            "上午好呀，记得多喝水 💧", "工作间隙伸个懒腰，灵感更闪耀。",
            "心静自然凉，事缓则圆。", "别太急，慢一点也很好。",
            "每个努力的上午，都值得被赞美。", "阳光正好，做自己想做的事。",
            "此刻努力，未来可期。", "你的笑，是午前最好的光。",
            "工作累了要伸伸腰～", "阳光正好，心情也要亮堂堂。",
            "去散个步吧，风会帮你解闷🍃", "今天也要吃好一点。",
            "别忘了微笑😊", "你的努力都被时间偷偷记着。",
            "多看窗外的天空，世界不止屏幕那么大。", "阳光透过树叶，你也会发光🌿",
            "偶尔犯懒也没关系。", "你不需要时时完美，只要时时真诚。",
            "心情不好？那就吃块甜的🍫", "小确幸藏在不经意的瞬间。",
            "别太忙着赶路，偶尔也看看风景。", "喝杯水，做个深呼吸，重启自己。",
            "愿你今天顺心、平安、被温柔包围。", "烦恼就让风带走吧。",
            "你的笑，真的很好看。", "心要像阳光一样，温暖而不刺眼。",
            "记得要开心。", "今天的云朵真可爱☁️", "多和自己对话，学会哄自己。",
            "平凡的日子，也可以很浪漫。", "希望你能被温柔对待，也能温柔对世界。",
            "你一定比自己想的更厉害。", "偶尔放空一下，大脑也需要休息。",
            "记得要照顾好自己，也要照顾好心。", "阳光下的你，是我最喜欢的样子。",
            "日子在继续，你要一直可爱。", "你是我见过的最温柔的白昼。",
            "上午的阳光不燥，正好适合努力与微笑。", "眼睛累啦？看看远处的绿树🌳",
            "我把上午的温柔，都藏在想你的时光里。",
            "和你分享的上午，才是最好的时光。", "想你时，风都有了方向。"
        ],

        "afternoon": [
            "小憩一刻，幸福不远 🌿", "别急，花会开，事会顺。", "世间温柔，总在不经意间出现。",
            "心怀浪漫宇宙，也珍惜人间日常 💫", "偶尔发呆，也是种治愈。", "忙碌之余，别忘了笑～",
            "青山不改，柔风相伴。", "阳光温柔，时光慢慢。", "午后的一抹甜，给心放个假 🍰",
            "愿君常安，心似花开。",
            "午后时光，温柔又慵懒 ☕", "小憩片刻，满血复活！",
            "光影浅浅，岁月安然。", "一点点困意，也藏着幸福。",
            "午后的风最懂人心。", "沉下心，做点喜欢的事。",
            "生活在慢慢发光，就像你一样。", "阳光落在你睫毛上，真好看。",
            "午后暖阳，岁月悠长，愿你安然无恙。", "一杯下午茶，治愈所有疲惫☕",
            "午后的小憩，是给身体最好的充电。", "阳光斜照，影子拉长，时光也变得温柔。",
            "午后的风带着慵懒，适合放空与思念。", "别让疲惫占据午后，给自己放松时间。",
            "午后的阳光透过窗帘，温柔得不像话。", "一杯果茶，一本好书，午后惬意时光。",
            "午后的宁静，是忙碌生活中的小确幸。", "困了就眯一会儿，不必勉强自己。",
            "午后的时光，适合回忆美好的事。", "阳光正好，微风不燥，午后真舒服。",
            "让午后的阳光晒走所有烦恼。", "偶尔的慵懒，是对生活的温柔妥协。",
            "午后的街道安静，心里也变得平和。", "做点喜欢的事，让午后更有意义。",
            "午后的光影斑驳，像一幅温柔的画。", "给朋友发个消息，分享午后的美好。",
            "午后的风轻轻吹，带来远方的思念。", "别着急赶路，享受此刻的宁静。",
            "午后的阳光洒在身上，温暖又治愈。", "一份甜点，一份快乐，午后甜蜜时光🍰",
            "午后的时光，适合整理心情，重新出发。", "让午后的宁静，抚平内心的浮躁。",
            "午后的你，值得被温柔对待。", "阳光正好，适合出门散散步。",
            "午后好，别忘了休息片刻☕", "疲惫是暂时的，光亮是永恒的。",
            "平凡的努力，也能闪光。", "你值得所有温柔。",
            "安静地做事，悄悄地发光。", "生活会慢慢变甜。",
            "心若有光，何惧路长。", "午后的风也在替我夸你。",
            "微笑，是最好的能量补给。", "相信过程，相信自己。"
        ],

        "evening": [
            "夕阳下的风，有点温柔～", "天色渐暗，心情渐柔 🌙", "愿你一日辛劳皆成收获。",
            "落霞与孤鹜齐飞，秋水共长天一色。", "不慌不忙，心自芬芳。", "今日的结束，是明日的开始。",
            "一壶清酒，一页旧梦。", "晚风吹散疲惫，星光点亮心扉。",
            "月上柳梢头，人约黄昏后 💫",
            "傍晚好！今日的风很柔。🌇", "天边的霞光，是世界对你的问候。",
            "收一收忙碌，留一点温柔。", "日落余晖，皆是生活的告白。",
            "晚风轻拂，烦恼也要散去。", "回家的路，最暖心。",
            "一天辛苦啦，笑一笑吧。", "晚霞和你，都温柔得刚刚好。",
            "傍晚的风最温柔，你也是🌇", "星星开始营业啦✨",
            "今天过得辛苦吗？歇歇吧～", "万物安静时，愿你也安然。",
            "天空换上了温柔滤镜。", "白天的喧嚣该落幕了。",
            "落日余晖，都是生活的柔情。",
            "不必完美，温柔就好。", "晚风轻抚，心也该慢下来。",
            "微风不燥，岁月静好。", "岁月从不辜负温柔的人。",
            "今夜无风无月，有你就足够了。", "灯火阑珊处，有人正念你。",
            "天边最后一抹光，也为你而亮。", "日落归山海，山海藏温柔。", "你是傍晚落日的颜色。",
            "浮生若梦，为欢几何。", "晚霞很美，你更美。", "我在人间贩卖黄昏，只为收集世间温柔。",
            "夜幕低垂，想念正浓。", "傍晚的风替我拥抱你，你感受到了吗？",

        ],

        "night": [
            "夜深了，放松心情 🌙", "月色真美，如你一般。",
            "星河灿烂，心中安然。", "今天的你，已经很棒啦。",
            "风轻，梦暖，好梦即将来临。", "夜色温柔，适合想念与平静。",
            "关掉烦恼，打开梦境。",
            "晚安，愿你有个甜甜的梦🍃", "今天也辛苦啦。",
            "卸下一天的疲惫，好好睡吧。", "世界晚安，星星亮了🌙",
            "所有的压力都留在梦外。", "心安即是归处。",
            "夜色温柔，你也要温柔待自己。", "闭上眼睛，星光在等你。",
            "愿你梦里有光，醒来有爱。", "别害怕黑夜，它只是梦的入口。",
            "有些温柔，不必言说。", "人生海海，静夜自明。",
            "慢一点，夜晚属于你。", "放下心事，拥抱睡意。",
            "窗外的月光，是我给你的问候。", "万物沉睡时，思念最轻也最真。",
            "人间寂静处，总有人在默默想你。", "如果你也在想我，那就太好了。",
            "夜色如墨，星光如钻，愿你好梦相伴🌙", "月光皎洁，思念如潮，愿你安好。",
            "夜深人静，心事渐明，愿你安然入睡。", "星光点点，夜色温柔，晚安我的爱。",
            "月光洒满地，思念藏心底。", "夜深了，别想太多，好好休息。",
            "希望你的梦里有风、有花，也有我。",
            "晚安，我的全世界，梦里见。",
            "星星知道我在想你，不信你抬头看看。",
            "多想此刻能看着你，说声晚安。",
            "夜色很好，看起来你也很好。"
        ],

        "midnight": [
            "夜色温柔，梦里都是你。", "星光不问赶路人，时光不负有心人 🌌",
            "灯火阑珊处，也许你在笑。", "今夜无眠，心安即梦。", "世界晚安，你要好梦 💭",
            "风停了，心也慢下来。", "夜雨寄北，梦回长安。", "长夜未央，愿君安然。", "梦里有花开，也有你的笑。",
            "此心安处，便是吾乡。",
            "深夜好，别熬太晚了 🌌", "此刻的宁静，是心的归宿。",
            "夜未央，心可安。", "风在轻轻吹，梦也轻轻来。",
            "要温柔地对待自己。", "晚安，世界；晚安，未来的希望。",
            "好梦入怀，心有光亮。", "此刻的星光，也想念你。",
            "夜半三更，万籁俱寂，愿你心有所安🌌", "深夜的宁静，是灵魂的栖息地。",
            "月光如水，夜色深沉，别熬夜了。", "深夜的风带着凉意，也带着思念。",
            "夜半无眠，思念如潮，愿你入梦。", "深夜的星空最璀璨，也最治愈。",
            "夜未央，人未眠，心事向谁言。", "深夜的宁静，适合思考人生。",
            "月光洒在窗台，深夜的美藏不住。", "夜半时分，愿你放下所有疲惫。",
            "深夜的风轻轻吹，带来远方的问候。", "星空浩瀚，夜色深沉，晚安。",
            "夜半无眠，思念正浓，愿你知晓。", "深夜的宁静，是对自己的温柔。",
            "月光皎洁，夜色深沉，愿你好梦。", "夜半三更，万籁俱寂，心也平静。",
            "深夜的思念最汹涌，你感受到了吗？", "想穿过黑夜，去到你的身边说晚安。",
            "深夜的星星都睡了，只有我的思念还醒着。"
        ]
    }

    period_tips = TIPS.get(period, ["愿你被温柔以待"])

    # 依次显示时间段提示词
    for tip in period_tips:
        t = threading.Thread(target=show_rounded_bubble, args=(tip,))
        t.daemon = True
        t.start()
        time.sleep(0.2)  # 每条提示间隔0.3秒

    # 显示几条通用温柔提示
    for tip in COMMON_TIPS:
        t = threading.Thread(target=show_rounded_bubble, args=(tip,))
        t.daemon = True
        t.start()
        time.sleep(0.2)

    # 最终居中提示
    def show_final():
        window = tk.Tk()
        window.overrideredirect(True)
        window.attributes("-topmost", True)
        window.attributes("-alpha", 0.0)
        sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
        w, h = 400, 150
        x, y = (sw-w)//2, (sh-h)//2
        window.geometry(f"{w}x{h}+{x}+{y}")

        canvas = tk.Canvas(window, width=w, height=h, highlightthickness=0, bg='white')
        canvas.pack(fill=tk.BOTH, expand=True)
        bg_color = "#FFD1DC"
        fg = get_text_color(bg_color)
        create_rounded_rect(canvas, 0, 0, w, h, radius=30, fill=bg_color, outline=bg_color)
        canvas.create_text(w/2, h/2, text=FINAL_MESSAGE, font=("圆体", 18), fill=fg, width=w-40)

        # 淡入淡出动画
        def animate_final():
            for i in range(21):
                window.attributes("-alpha", i/20)
                time.sleep(0.05)
            time.sleep(3)
            for i in range(20, -1, -1):
                window.attributes("-alpha", i/20)
                time.sleep(0.05)
            window.destroy()

        threading.Thread(target=animate_final, daemon=True).start()
        window.mainloop()

    # 延迟 3 秒再显示最终提示
    threading.Timer(5, show_final).start()

if __name__ == "__main__":
    print("程序启动中...")
    launch_all_bubbles()

