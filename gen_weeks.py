import json, os

OUT = "/sessions/brave-loving-galileo/mnt/outputs"

# ── Vocabulary data by week ─────────────────────────────────────────────────
WEEKS = {
  "week2": {
    "title": "Week 2", "subtitle": "食物・健康・地理",
    "cats": {
      "food":   {"name":"食物/飲料","e":"🍎","words":[
        ("apple","蘋果","🍎"),("banana","香蕉","🍌"),("beef","牛肉","🥩"),
        ("bread","麵包","🍞"),("breakfast","早餐","🍳"),("cake","蛋糕","🎂"),
        ("candy","糖果","🍬"),("chicken","雞肉","🍗"),("chocolate","巧克力","🍫"),
        ("coffee","咖啡","☕"),("cola","可樂","🥤"),("cook","做飯","👨‍🍳"),
        ("cookies","餅乾","🍪"),("dinner","晚餐","🍽️"),("drink","喝","💧"),
        ("duck","鴨肉","🦆"),("dumpling","水餃","🥟"),("eat","吃","😋"),
        ("egg","蛋","🥚"),("fish","魚肉","🐟"),("food","食物","🍱"),
        ("French fries","薯條","🍟"),("fruit","水果","🍑"),("full","飽的","😌"),
        ("grape","葡萄","🍇"),("hamburger","漢堡","🍔"),("hungry","餓的","😋"),
        ("ice cream","冰淇淋","🍦"),("juice","果汁","🧃"),("lemon","檸檬","🍋"),
        ("lunch","午餐","🥗"),("meal","餐","🍽️"),("milk","牛奶","🥛"),
        ("noodles","麵","🍜"),("orange","橘子","🍊"),("peach","桃子","🍑"),
        ("pie","派","🥧"),("pizza","披薩","🍕"),("pork","豬肉","🥩"),
        ("pumpkin","南瓜","🎃"),("rice","米飯","🍚"),("salad","沙拉","🥗"),
        ("sandwich","三明治","🥪"),("soup","湯","🍲"),("strawberry","草莓","🍓"),
        ("sweet","甜的","🍭"),("taste","嚐起來","👅"),("tea","茶","🍵"),
        ("thirsty","口渴的","💧"),("water","水","💧"),("watermelon","西瓜","🍉"),
        ("yummy","美味的","😋"),
      ]},
      "titles": {"name":"稱謂","e":"👔","words":[
        ("Miss","小姐","👩"),("Mr.","先生","👨"),("Mrs.","太太","👩"),("name","名字","📛"),
      ]},
      "geo":    {"name":"地理名詞","e":"🌍","words":[
        ("beach","海灘","🏖️"),("lake","湖","🏞️"),("mountain","山","⛰️"),
        ("river","河流","🌊"),("sea","大海","🌊"),
      ]},
      "health": {"name":"健康","e":"🏥","words":[
        ("cold","感冒","🤧"),("headache","頭痛","🤕"),("sick","生病的","😷"),
        ("strong","強壯的","💪"),("tired","疲累的","😴"),("toothache","牙痛","🦷"),
        ("well","好的；健康地","😊"),
      ]},
      "money":  {"name":"金錢","e":"💰","words":[
        ("buy","買","🛒"),("dollar","元","💵"),("free","免費的","🎁"),("money","錢","💰"),
      ]},
    }
  },

  "week3": {
    "title": "Week 3", "subtitle": "房子・數字",
    "cats": {
      "house": {"name":"房子/公寓","e":"🏠","words":[
        ("bathroom","浴室","🚿"),("bed","床","🛏️"),("bedroom","臥房","🛏️"),
        ("chair","椅子","🪑"),("clean","乾淨的；清理","✨"),("computer","電腦","💻"),
        ("desk","桌子","🪑"),("dining room","餐廳","🍽️"),("door","門","🚪"),
        ("fan","電扇","💨"),("floor","地板","🪟"),("fridge","電冰箱","🧊"),
        ("garden","院子、花園","🌷"),("home","家庭","🏠"),("house","房子","🏠"),
        ("key","鑰匙","🔑"),("kitchen","廚房","🍳"),("lamp","燈","💡"),
        ("living room","客廳","🛋️"),("mop","用拖把拖地","🧹"),
        ("refrigerator","電冰箱","🧊"),("shelf","架子","📚"),("shower","淋浴","🚿"),
        ("sofa","沙發","🛋️"),("street","街道","🏙️"),("sweep","掃","🧹"),
        ("table","桌子","🪑"),("telephone","電話","📞"),("television","電視","📺"),
        ("towel","毛巾","🏊"),("TV","電視","📺"),("wall","牆壁","🧱"),
        ("wash","洗","🚿"),("window","窗戶","🪟"),
      ]},
      "numbers": {"name":"數字","e":"🔢","words":[
        ("zero","零","0️⃣"),("one","一","1️⃣"),("two","二","2️⃣"),("three","三","3️⃣"),
        ("four","四","4️⃣"),("five","五","5️⃣"),("six","六","6️⃣"),("seven","七","7️⃣"),
        ("eight","八","8️⃣"),("nine","九","9️⃣"),("ten","十","🔟"),
        ("eleven","十一","🔢"),("twelve","十二","🔢"),("thirteen","十三","🔢"),
        ("fourteen","十四","🔢"),("fifteen","十五","🔢"),("sixteen","十六","🔢"),
        ("seventeen","十七","🔢"),("eighteen","十八","🔢"),("nineteen","十九","🔢"),
        ("twenty","二十","🔢"),("thirty","三十","🔢"),("forty","四十","🔢"),
        ("fifty","五十","🔢"),("sixty","六十","🔢"),("seventy","七十","🔢"),
        ("eighty","八十","🔢"),("ninety","九十","🔢"),("hundred","一百","💯"),
        ("first","第一","🥇"),("second","第二","🥈"),("third","第三","🥉"),
        ("last","最後的","🏁"),("all","全部的","🌟"),("both","兩個都","👫"),
        ("many","許多","✨"),("more","較多","➕"),("much","許多","✨"),
        ("number","數字","🔢"),("some","一些","✨"),
      ]},
    }
  },

  "week4": {
    "title": "Week 4", "subtitle": "形容詞・副詞・名詞・動詞",
    "cats": {
      "adj": {"name":"其他形容詞","e":"💫","words":[
        ("cool","清涼的","😎"),("different","不一樣的","🔄"),("dirty","髒的","🗑️"),
        ("easy","簡單的","😊"),("favorite","最喜歡的","❤️"),("fine","很不錯的","👍"),
        ("fun","有趣的","🎉"),("great","很棒的","🌟"),("hard","困難的","😓"),
        ("hot","燙的","🔥"),("interesting","有趣的","🤔"),("new","新的","✨"),
        ("OK","好的","👌"),("quiet","安靜的","🤫"),("ready","準備好的","✅"),
        ("right","對的","✓"),("sorry","感到抱歉的","😔"),("sure","確定的","✅"),
        ("wet","濕的","💧"),("wonderful","很棒的","🌟"),
      ]},
      "adv": {"name":"其他副詞","e":"⚡","words":[
        ("again","再一次","🔄"),("always","總是、永遠","♾️"),("maybe","也許","🤔"),
        ("never","不曾","🚫"),("sometimes","有時候","⏱️"),("together","一起","🤝"),
        ("usually","通常","📅"),
      ]},
      "nouns": {"name":"其他名詞","e":"📦","words":[
        ("birthday","生日","🎂"),("bottle","瓶子","🍶"),("box","箱子","📦"),
        ("can","罐子","🥫"),("cellphone","手機","📱"),("dream","夢","💤"),
        ("email","電子郵件","📧"),("flower","花","🌸"),("gift","禮物","🎁"),
        ("mail","信","✉️"),("party","派對","🎉"),("photo","照片","📷"),
        ("robot","機器人","🤖"),("sale","拍賣、特價","🏷️"),("thing","東西","📦"),
        ("ticket","票","🎫"),("trash","垃圾","🗑️"),("tree","樹","🌳"),
        ("way","路、方向","🗺️"),("word","字","📝"),
      ]},
      "verbs": {"name":"其他動詞","e":"🏃","words":[
        ("brush","用刷子刷","🪥"),("call","打電話給","📞"),("close","關","🚪"),
        ("come","來","👋"),("cry","哭泣","😢"),("do","做","✅"),
        ("enjoy","享受","😊"),("fall","掉落","🍂"),("feel","感覺","💭"),
        ("get","得到","🎁"),("give","給","🤲"),("go","去、走","🚶"),
        ("have","有","✋"),("help","幫助","🤝"),("hit","打、碰撞","👊"),
        ("hope","希望","🙏"),("hurry","趕快、急忙","🏃"),("hurt","受傷","🤕"),
        ("jump","跳","🦘"),("know","知道、認識","💡"),("laugh","笑","😄"),
        ("like","喜歡","❤️"),("look","看、看起來","👀"),("love","愛","❤️"),
        ("make","做、製造","🔨"),("meet","遇見、會面","👋"),("miss","想念","💭"),
        ("need","需要","✋"),("open","開","🚪"),("pick up","撿起、接電話","📞"),
        ("put","放","📦"),("see","看見","👀"),("show","展示","👁️"),
        ("sit","坐下","🪑"),("sleep","睡覺","😴"),("smell","聞起來","👃"),
      ]},
    }
  },

  "week5": {
    "title": "Week 5", "subtitle": "人・個性・地點",
    "cats": {
      "people": {"name":"人","e":"👥","words":[
        ("baby","嬰兒","👶"),("boy","男孩","👦"),("girl","女孩","👧"),
        ("kid","小孩","🧒"),("man","男人","👨"),("men","男人（複數）","👨‍👨"),
        ("people","人（複數）","👥"),("person","人","🧑"),
        ("woman","女人","👩"),("women","女人（複數）","👩‍👩"),
      ]},
      "personality": {"name":"個性/特點","e":"😊","words":[
        ("angry","生氣的","😡"),("bad","壞的","😈"),("beautiful","美麗的","😍"),
        ("bored","覺得無聊的","😒"),("boring","令人無聊的","😴"),("busy","忙碌的","💼"),
        ("cute","可愛的","🥰"),("excited","覺得興奮的","🤩"),("exciting","令人興奮的","🎉"),
        ("good","好的","😊"),("happy","開心的","😄"),("heavy","（人）重的","⚖️"),
        ("lazy","懶惰的","😪"),("mad","生氣的","😤"),("nice","令人愉快的","😊"),
        ("old","老的","👴"),("pretty","漂亮的","💄"),("sad","傷心的","😢"),
        ("short","矮的","📏"),("smart","聰明的","🧠"),("tall","高的","🦒"),
        ("thin","瘦的","🪶"),("young","年輕的","🌱"),
      ]},
      "places": {"name":"地點/方位","e":"📍","words":[
        ("back","向後、回原處","↩️"),("bank","銀行","🏦"),("bookstore","書店","📚"),
        ("department store","百貨公司","🏬"),("fire station","消防站","🚒"),
        ("here","這裡","📍"),("hospital","醫院","🏥"),("Japan","日本","🗾"),
        ("left","左邊（的）","⬅️"),("market","市場","🛒"),("movie theater","電影院","🎬"),
      ]},
    }
  },

  "week6": {
    "title": "Week 6", "subtitle": "學校・尺寸・運動・餐具",
    "cats": {
      "school": {"name":"學校","e":"🏫","words":[
        ("read","閱讀","📖"),("ruler","尺","📏"),("say","說","💬"),
        ("school","學校","🏫"),("science","科學","🔬"),("speak","說","💬"),
        ("spell","拼寫","🔤"),("story","故事","📚"),("student","學生","🎒"),
        ("study","學習","📚"),("talk","說話、談話","💬"),("teacher","老師","👩‍🏫"),
        ("test","考試","📝"),("vacation","假期","🌴"),("write","寫","✏️"),
      ]},
      "size": {"name":"尺寸/丈量","e":"📏","words":[
        ("big","大的","🔵"),("heavy","（物品）重的","⚖️"),("high","高的","⬆️"),
        ("light","輕的","🪶"),("long","長的","📏"),("pair","一雙、一對","👟"),
        ("short","短的","📏"),("small","小的","🔹"),
      ]},
      "sports": {"name":"運動/興趣","e":"⚽","words":[
        ("ball","球","⚽"),("baseball","棒球","⚾"),("basketball","籃球","🏀"),
        ("card","卡片","🃏"),("climb","爬、攀爬","🧗"),("dance","跳舞","💃"),
        ("doll","玩偶","🪆"),("drum","鼓","🥁"),("fish","釣魚","🎣"),
        ("game","遊戲、比賽","🎮"),("hike","健行","🥾"),("kite","風箏","🪁"),
        ("movie","電影","🎬"),("paint","用顏料畫","🎨"),("piano","鋼琴","🎹"),
        ("play","玩","🎮"),("run","跑、跑步","🏃"),("sing","唱歌","🎤"),
        ("soccer","足球","⚽"),("song","歌曲","🎵"),("sport","運動","🏅"),
        ("swim","游泳","🏊"),("toy","玩具","🧸"),("trip","短程旅行","✈️"),
        ("win","贏","🏆"),("yo-yo","溜溜球","🪀"),
      ]},
      "utensils": {"name":"餐具","e":"🍴","words":[
        ("chopsticks","筷子","🥢"),("cup","杯子","☕"),("dish","碟子、盤子","🍽️"),
        ("fork","叉子","🍴"),("glass","玻璃杯","🥛"),("knife","刀子","🔪"),
        ("spoon","湯匙","🥄"),
      ]},
    }
  },

  "week7": {
    "title": "Week 7", "subtitle": "時間・日期・季節",
    "cats": {
      "time": {"name":"時間","e":"⏰","words":[
        ("afternoon","下午","🌅"),("April","四月","🌸"),("August","八月","☀️"),
        ("clock","時鐘","🕐"),("day","天","📅"),("December","十二月","❄️"),
        ("early","早到（的）","⏰"),("evening","傍晚","🌆"),("fall","秋天","🍂"),
        ("February","二月","❤️"),("Friday","星期五","📅"),("January","一月","🎊"),
        ("July","七月","🌞"),("June","六月","🌤️"),("late","晚到（的）","🕐"),
        ("March","三月","🌱"),("May","五月","🌻"),("Monday","星期一","📅"),
        ("month","月","📅"),("morning","早上","🌅"),("night","晚上","🌙"),
        ("November","十一月","🍁"),("now","現在","⏱️"),("o'clock","…點鐘","🕐"),
        ("October","十月","🎃"),("Saturday","星期六","🎉"),("season","季節","🍂"),
        ("September","九月","📚"),("spring","春天","🌸"),("summer","夏天","☀️"),
        ("Sunday","星期日","😊"),("Thursday","星期四","📅"),("time","時間","⏰"),
        ("today","今天","📅"),("tomorrow","明天","➡️"),("Tuesday","星期二","📅"),
        ("watch","手錶","⌚"),("Wednesday","星期三","📅"),("week","星期","📅"),
        ("winter","冬天","❄️"),("year","年","📅"),("yesterday","昨天","⬅️"),
      ]},
    }
  },

  "week8": {
    "title": "Week 8", "subtitle": "工作・職業",
    "cats": {
      "jobs": {"name":"工作","e":"💼","words":[
        ("actor","男演員","🎭"),("actress","女演員","🎭"),("cook","廚師","👨‍🍳"),
        ("doctor","醫生","👨‍⚕️"),("driver","司機、駕駛員","🚗"),("farmer","農夫","👨‍🌾"),
        ("job","工作、職業","💼"),("mailman","郵差","📮"),("nurse","護士","👩‍⚕️"),
        ("police officer","警察","👮"),("singer","歌手","🎤"),("soldier","軍人","🪖"),
        ("waiter","男服務生","🤵"),("waitress","女服務生","🤵"),
        ("work","工作","💼"),("worker","工作者","👷"),
      ]},
    }
  },
}

# ── HTML template ──────────────────────────────────────────────────────────
def make_v_obj(cats):
    parts = []
    for key, cat in cats.items():
        words_js = ",\n    ".join(
            f'{{en:{json.dumps(w[0])},zh:{json.dumps(w[1])},e:{json.dumps(w[2])}}}'
            for w in cat["words"]
        )
        parts.append(
            f'  {key}:{{name:{json.dumps(cat["name"])},e:{json.dumps(cat["e"])},words:[\n    {words_js},\n  ]}}'
        )
    return "const V = {\n" + ",\n".join(parts) + "\n};"

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>⭐ {title} 美語單字練習</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--yellow:#FFD93D;--orange:#FF9F43;--pink:#FF6B9D;--purple:#A29BFE;--blue:#48DBFB;--green:#55EFC4;--red:#FF7675;--correct:#00B894;--wrong:#D63031}}
body{{font-family:'Segoe UI','Microsoft JhengHei',Arial,sans-serif;background:linear-gradient(135deg,{bg1} 0%,{bg2} 45%,{bg3} 100%);min-height:100vh;padding:14px}}
.container{{max-width:480px;margin:0 auto}}
.screen{{display:none}}.screen.active{{display:block;animation:fadeUp .3s ease}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:translateY(0)}}}}
.home-hero{{text-align:center;padding:18px 0 22px}}
.home-hero .stars-row{{font-size:2rem;letter-spacing:4px;margin-bottom:6px}}
.home-hero h1{{font-size:1.9rem;color:#E91E63;line-height:1.2;margin-bottom:4px;text-shadow:2px 2px 0 #FCE4EC}}
.home-hero .week-badge{{display:inline-block;background:#FFD93D;color:#555;padding:3px 14px;border-radius:50px;font-size:.85rem;font-weight:700;margin-bottom:4px}}
.home-hero p{{color:#888;font-size:.88rem}}
.sec-label{{font-size:1rem;font-weight:700;color:#555;margin:14px 0 8px;display:flex;align-items:center;gap:6px}}
.cat-row{{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;-webkit-overflow-scrolling:touch}}
.cat-row::-webkit-scrollbar{{height:3px}}.cat-row::-webkit-scrollbar-thumb{{background:#ddd;border-radius:2px}}
.cat-btn{{flex-shrink:0;padding:9px 16px;border-radius:50px;border:2.5px solid #DDD;background:white;font-size:.88rem;font-weight:700;color:#666;cursor:pointer;transition:all .2s;white-space:nowrap}}
.cat-btn:hover{{border-color:#bbb;transform:translateY(-1px)}}
.cat-btn.sel{{background:var(--orange);border-color:#E07B1E;color:#fff}}
.cat-btn.sel[data-cat="all"]{{background:#FFD93D;border-color:#F0B800;color:#555}}
.word-count{{text-align:center;color:#AAA;font-size:.82rem;margin:4px 0 12px}}
.mode-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.mode-card{{background:white;border-radius:18px;padding:18px 12px;text-align:center;border:2.5px solid #EEE;cursor:pointer;transition:all .2s;box-shadow:0 3px 10px rgba(0,0,0,.06)}}
.mode-card:hover{{transform:translateY(-4px);box-shadow:0 8px 20px rgba(0,0,0,.12)}}
.mode-card[data-mode="flashcard"]{{border-color:#FFD93D}}.mode-card[data-mode="quiz"]{{border-color:#48DBFB}}
.mode-card[data-mode="spell"]{{border-color:#FF9F43}}.mode-card[data-mode="match"]{{border-color:#A29BFE}}
.mode-ico{{font-size:2rem}}.mode-name{{font-size:.95rem;font-weight:700;color:#333;margin:7px 0 3px}}.mode-desc{{font-size:.75rem;color:#999}}
.g-header{{display:flex;align-items:center;gap:10px;margin-bottom:14px}}
.back-btn{{background:white;border:none;border-radius:50%;width:42px;height:42px;font-size:1.3rem;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.back-btn:hover{{background:#f5f5f5}}
.g-title{{font-size:1rem;font-weight:700;color:#555}}
.score-pill{{margin-left:auto;background:#FFD93D;color:#555;padding:5px 14px;border-radius:50px;font-weight:700;font-size:.88rem}}
.prog-wrap{{background:#EEE;border-radius:50px;height:9px;margin-bottom:6px;overflow:hidden}}
.prog-bar{{height:100%;border-radius:50px;background:linear-gradient(90deg,#FFD93D,#FF9F43);transition:width .4s ease}}
.prog-txt{{text-align:center;color:#AAA;font-size:.8rem;margin-bottom:14px}}
.speak-btn{{background:none;border:none;font-size:1.4rem;cursor:pointer;opacity:.7;transition:opacity .2s;padding:4px}}.speak-btn:hover{{opacity:1}}
.fc-wrap{{perspective:1200px;margin:0 auto 20px;max-width:400px}}
.fc{{width:100%;padding-top:60%;position:relative;cursor:pointer;transform-style:preserve-3d;transition:transform .5s ease}}
.fc.flipped{{transform:rotateY(180deg)}}
.fc-face{{position:absolute;top:0;left:0;right:0;bottom:0;border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;backface-visibility:hidden;-webkit-backface-visibility:hidden;padding:20px}}
.fc-front{{background:linear-gradient(135deg,#FFFDE7,#FFF3E0);border:2.5px solid #FFD93D;box-shadow:0 6px 20px rgba(255,200,0,.18)}}
.fc-back{{background:linear-gradient(135deg,#E8F5E9,#E3F2FD);border:2.5px solid #48DBFB;box-shadow:0 6px 20px rgba(72,219,251,.18);transform:rotateY(180deg)}}
.fc-emoji{{font-size:3.5rem;margin-bottom:10px}}.fc-word{{font-size:1.9rem;font-weight:700;color:#333}}
.fc-zh{{font-size:1.8rem;font-weight:700;color:#2C3E50}}.fc-en-small{{font-size:1.1rem;color:#888;margin-top:6px}}
.fc-hint{{font-size:.82rem;color:#BBB;margin-top:10px}}.fc-cat{{font-size:.75rem;color:#CCC;margin-top:4px}}
.fc-btns{{display:flex;gap:10px;max-width:400px;margin:0 auto}}.fc-btns.hidden{{visibility:hidden}}
.btn-review{{flex:1;padding:13px;border:none;border-radius:14px;font-size:.95rem;font-weight:700;cursor:pointer;background:#FFD93D;color:#7D5A00;box-shadow:0 3px 10px rgba(255,217,61,.3);transition:all .2s}}
.btn-learned{{flex:1;padding:13px;border:none;border-radius:14px;font-size:.95rem;font-weight:700;cursor:pointer;background:#55EFC4;color:#1a6040;box-shadow:0 3px 10px rgba(85,239,196,.3);transition:all .2s}}
.btn-review:hover,.btn-learned:hover{{transform:translateY(-2px)}}
.dir-toggle{{display:flex;background:white;border-radius:50px;padding:3px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
.dir-btn{{flex:1;padding:8px;border:none;border-radius:50px;font-size:.82rem;font-weight:700;cursor:pointer;background:transparent;color:#999;transition:all .2s}}
.dir-btn.active{{background:#48DBFB;color:#333}}
.quiz-q-box{{background:white;border-radius:18px;padding:24px 16px;text-align:center;margin-bottom:16px;box-shadow:0 3px 14px rgba(0,0,0,.07)}}
.quiz-q-emoji{{font-size:2.8rem;margin-bottom:8px}}.quiz-q-word{{font-size:1.8rem;font-weight:700;color:#333}}.quiz-q-lbl{{font-size:.8rem;color:#BBB;margin-top:4px}}
.quiz-opts{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}}
.quiz-opt{{padding:14px 10px;border-radius:14px;border:2.5px solid #E5E5E5;background:white;font-size:.95rem;font-weight:700;color:#333;cursor:pointer;transition:all .2s;line-height:1.3;box-shadow:0 2px 8px rgba(0,0,0,.05)}}
.quiz-opt:hover:not(:disabled){{border-color:#48DBFB;transform:translateY(-2px)}}.quiz-opt.correct{{background:#55EFC4;border-color:#00B894;color:#1a6040}}.quiz-opt.wrong{{background:#FF7675;border-color:#D63031;color:#fff}}.quiz-opt:disabled{{cursor:not-allowed}}
.spell-q-box{{background:white;border-radius:18px;padding:24px 16px;text-align:center;margin-bottom:16px;box-shadow:0 3px 14px rgba(0,0,0,.07)}}
.spell-emoji{{font-size:3.2rem;margin-bottom:6px}}.spell-zh{{font-size:1.9rem;font-weight:700;color:#333}}
.spell-area{{max-width:360px;margin:0 auto}}
.spell-input{{width:100%;padding:13px 16px;border-radius:14px;border:2.5px solid #DDD;font-size:1.3rem;font-weight:700;text-align:center;outline:none;margin-bottom:10px;transition:border-color .2s;letter-spacing:1px}}
.spell-input:focus{{border-color:#FF9F43}}.spell-input.correct{{border-color:#00B894;background:#E8F5E9}}.spell-input.wrong{{border-color:#D63031;background:#FFEBEE}}
.spell-btns{{display:flex;gap:8px;margin-bottom:10px}}
.btn-hint{{padding:11px 16px;border-radius:12px;border:2px solid #FFD93D;background:white;color:#7D5A00;font-weight:700;font-size:.88rem;cursor:pointer}}.btn-hint:hover{{background:#FFFDE7}}
.btn-submit{{flex:1;padding:11px;border-radius:12px;border:none;background:#FF9F43;color:white;font-weight:700;font-size:.95rem;cursor:pointer;box-shadow:0 3px 10px rgba(255,159,67,.3);transition:all .2s}}.btn-submit:hover{{transform:translateY(-2px)}}
.spell-feedback{{text-align:center;font-size:1rem;font-weight:700;padding:9px;border-radius:12px;margin-bottom:10px;display:none}}
.spell-feedback.ok{{background:#E8F5E9;color:#2D6A4F;display:block}}.spell-feedback.no{{background:#FFEBEE;color:#B71C1C;display:block}}
.btn-next-spell{{width:100%;padding:13px;border-radius:14px;border:none;background:#A29BFE;color:white;font-size:1rem;font-weight:700;cursor:pointer;box-shadow:0 3px 10px rgba(162,155,254,.3);display:none}}
.btn-next-spell.show{{display:block}}
.match-hint{{text-align:center;color:#999;font-size:.85rem;margin-bottom:10px}}
.match-cols{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:6px}}
.match-col-lbl{{text-align:center;font-size:.8rem;font-weight:700;color:#AAA}}
.match-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:16px}}
.m-tile{{padding:12px 8px;border-radius:12px;border:2.5px solid #E5E5E5;background:white;text-align:center;font-weight:700;font-size:.9rem;cursor:pointer;transition:all .2s;box-shadow:0 2px 8px rgba(0,0,0,.05);min-height:54px;display:flex;align-items:center;justify-content:center;line-height:1.3}}
.m-tile:hover:not(.matched):not(.disabled){{transform:translateY(-2px);border-color:#A29BFE}}.m-tile.sel{{border-color:#6C5CE7;background:#EDE9FE}}
.m-tile.matched{{background:#E8F5E9;border-color:#00B894;color:#2D6A4F;opacity:.65;cursor:default}}
.m-tile.shake{{animation:shake .4s ease}}.m-tile.wrong-fl{{background:#FFEBEE;border-color:#D63031}}
@keyframes shake{{0%,100%{{transform:translateX(0)}}20%{{transform:translateX(-6px)}}40%{{transform:translateX(6px)}}60%{{transform:translateX(-4px)}}80%{{transform:translateX(4px)}}}}
.results-wrap{{text-align:center;padding:16px 0}}.res-big{{font-size:5rem;margin-bottom:12px}}.res-title{{font-size:1.5rem;font-weight:700;color:#333;margin-bottom:6px}}.res-sub{{color:#999;margin-bottom:20px;font-size:.9rem}}
.res-box{{background:white;border-radius:22px;padding:22px;margin-bottom:22px;box-shadow:0 4px 16px rgba(0,0,0,.07)}}.res-num{{font-size:2.8rem;font-weight:700;color:#E91E63}}.res-lbl{{color:#AAA;font-size:.85rem;margin-top:2px}}.res-stars{{font-size:2rem;margin-top:12px}}
.res-btns{{display:flex;flex-direction:column;gap:10px}}
.btn-again{{padding:15px;border-radius:16px;border:none;background:#FFD93D;color:#555;font-size:1rem;font-weight:700;cursor:pointer;box-shadow:0 3px 10px rgba(255,217,61,.3);transition:all .2s}}.btn-again:hover{{transform:translateY(-2px)}}
.btn-home{{padding:13px;border-radius:16px;border:2.5px solid #EEE;background:white;color:#666;font-size:.95rem;font-weight:700;cursor:pointer}}.btn-home:hover{{background:#f9f9f9}}
@media(max-width:360px){{.fc-word,.fc-zh{{font-size:1.5rem}}.quiz-q-word{{font-size:1.5rem}}.quiz-opt{{font-size:.85rem;padding:11px 6px}}}}
@media(min-width:520px){{.home-hero h1{{font-size:2.3rem}}.fc-word{{font-size:2.2rem}}.fc-emoji{{font-size:4rem}}}}
</style>
</head>
<body>
<div class="container">
<div id="scr-home" class="screen active">
  <div class="home-hero">
    <div class="stars-row">🌟✨⭐</div>
    <div class="week-badge">{title}</div>
    <h1>美語單字<br>練習</h1>
    <p>{subtitle}</p>
  </div>
  <div class="sec-label">📚 選擇分類</div>
  <div class="cat-row" id="cat-row"></div>
  <div class="word-count" id="wcount"></div>
  <div class="sec-label">🎮 選擇遊戲模式</div>
  <div class="mode-grid">
    <div class="mode-card" data-mode="flashcard"><div class="mode-ico">📖</div><div class="mode-name">閃卡複習</div><div class="mode-desc">翻牌學單字</div></div>
    <div class="mode-card" data-mode="quiz"><div class="mode-ico">🎯</div><div class="mode-name">選擇題</div><div class="mode-desc">選出正確答案</div></div>
    <div class="mode-card" data-mode="spell"><div class="mode-ico">🔤</div><div class="mode-name">拼字挑戰</div><div class="mode-desc">打出英文單字</div></div>
    <div class="mode-card" data-mode="match"><div class="mode-ico">🧩</div><div class="mode-name">配對遊戲</div><div class="mode-desc">英文配中文</div></div>
  </div>
</div>
<div id="scr-flashcard" class="screen">
  <div class="g-header"><button class="back-btn" onclick="goHome()">←</button><span class="g-title">📖 閃卡複習</span><span class="score-pill" id="fc-score">✅ 0</span></div>
  <div class="prog-wrap"><div class="prog-bar" id="fc-prog" style="width:0%"></div></div>
  <div class="prog-txt" id="fc-ptxt">第 1 / ? 張</div>
  <div class="fc-wrap">
    <div class="fc" id="fc" onclick="flipCard()">
      <div class="fc-face fc-front">
        <div class="fc-emoji" id="fc-emo">🌟</div>
        <div class="fc-word" id="fc-word">word</div>
        <div style="margin-top:8px;display:flex;align-items:center;gap:6px"><button class="speak-btn" onclick="event.stopPropagation();speak()" title="朗讀">🔊</button></div>
        <div class="fc-hint">點擊翻牌看中文 👆</div>
        <div class="fc-cat" id="fc-cat"></div>
      </div>
      <div class="fc-face fc-back">
        <div class="fc-emoji" id="fc-emo2">🌟</div>
        <div class="fc-zh" id="fc-zh">中文</div>
        <div class="fc-en-small" id="fc-word2">word</div>
      </div>
    </div>
  </div>
  <div class="fc-btns hidden" id="fc-btns">
    <button class="btn-review" onclick="fcAct(\'review\')">🔄 再複習</button>
    <button class="btn-learned" onclick="fcAct(\'learned\')">✅ 記住了！</button>
  </div>
</div>
<div id="scr-quiz" class="screen">
  <div class="g-header"><button class="back-btn" onclick="goHome()">←</button><span class="g-title">🎯 選擇題</span><span class="score-pill" id="q-score">⭐ 0</span></div>
  <div class="dir-toggle">
    <button class="dir-btn active" id="d-zh" onclick="setDir(\'zh2en\')">看中文選英文</button>
    <button class="dir-btn" id="d-en" onclick="setDir(\'en2zh\')">看英文選中文</button>
  </div>
  <div class="prog-wrap"><div class="prog-bar" id="q-prog" style="width:0%"></div></div>
  <div class="prog-txt" id="q-ptxt">第 1 / 20 題</div>
  <div class="quiz-q-box">
    <div class="quiz-q-emoji" id="q-emo">🌟</div>
    <div class="quiz-q-word" id="q-word">word</div>
    <div style="display:flex;align-items:center;justify-content:center;gap:6px;margin-top:4px"><button class="speak-btn" id="q-speak-btn" onclick="speakQW()" style="display:none" title="朗讀">🔊</button></div>
    <div class="quiz-q-lbl" id="q-lbl">這個中文是什麼英文？</div>
  </div>
  <div class="quiz-opts" id="q-opts">
    <button class="quiz-opt"></button><button class="quiz-opt"></button>
    <button class="quiz-opt"></button><button class="quiz-opt"></button>
  </div>
</div>
<div id="scr-spell" class="screen">
  <div class="g-header"><button class="back-btn" onclick="goHome()">←</button><span class="g-title">🔤 拼字挑戰</span><span class="score-pill" id="sp-score">⭐ 0</span></div>
  <div class="prog-wrap"><div class="prog-bar" id="sp-prog" style="width:0%"></div></div>
  <div class="prog-txt" id="sp-ptxt">第 1 / 20 題</div>
  <div class="spell-q-box"><div class="spell-emoji" id="sp-emo">🌟</div><div class="spell-zh" id="sp-zh">中文</div></div>
  <div class="spell-area">
    <input type="text" class="spell-input" id="sp-inp" placeholder="輸入英文..." autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"/>
    <div class="spell-btns"><button class="btn-hint" onclick="spHint()">💡 提示</button><button class="btn-submit" onclick="checkSpell()">確認 ✓</button></div>
    <div class="spell-feedback" id="sp-fb"></div>
    <button class="btn-next-spell" id="sp-next" onclick="nextSpell()">下一題 →</button>
  </div>
</div>
<div id="scr-match" class="screen">
  <div class="g-header"><button class="back-btn" onclick="goHome()">←</button><span class="g-title">🧩 配對遊戲</span><span class="score-pill" id="mt-score">✅ 0/4</span></div>
  <div class="prog-wrap"><div class="prog-bar" id="mt-prog" style="width:0%"></div></div>
  <div class="prog-txt" id="mt-ptxt">第 1 / ? 輪</div>
  <div class="match-hint">點英文單字，再點對應的中文！</div>
  <div class="match-cols"><div class="match-col-lbl">🔤 英文</div><div class="match-col-lbl">🈳 中文</div></div>
  <div class="match-grid" id="mt-grid"></div>
</div>
<div id="scr-results" class="screen">
  <div class="results-wrap">
    <div class="res-big" id="res-ico">🎉</div>
    <div class="res-title" id="res-title">太棒了！</div>
    <div class="res-sub" id="res-sub">練習完成！</div>
    <div class="res-box"><div class="res-num" id="res-num">0/0</div><div class="res-lbl" id="res-lbl">答對題數</div><div class="res-stars" id="res-stars">⭐⭐⭐</div></div>
    <div class="res-btns"><button class="btn-again" onclick="restart()">🔄 再玩一次</button><button class="btn-home" onclick="goHome()">🏠 回首頁</button></div>
  </div>
</div>
</div>
<script>
{V_OBJ}
function shuffle(a){{const r=[...a];for(let i=r.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[r[i],r[j]]=[r[j],r[i]]}}return r}}
function getWords(cat){{return cat==='all'?Object.values(V).flatMap(c=>c.words):[...V[cat].words]}}
function getCat(en){{for(const[k,v]of Object.entries(V)){{if(v.words.some(w=>w.en===en))return v.name}}return''}}
function showScr(id){{document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));document.getElementById('scr-'+id).classList.add('active')}}
function goHome(){{showScr('home')}}
function speak(txt){{const t=txt||document.getElementById('fc-word').textContent;if(!window.speechSynthesis)return;const u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=0.85;speechSynthesis.cancel();speechSynthesis.speak(u)}}
let S={{cat:'all',mode:null,words:[]}};
// ── Build category buttons ──
(function(){{
  const row=document.getElementById('cat-row');
  const allBtn=document.createElement('button');
  allBtn.className='cat-btn sel';allBtn.dataset.cat='all';allBtn.textContent='🌟 全部';
  allBtn.addEventListener('click',()=>selCat('all',allBtn));
  row.appendChild(allBtn);
  Object.entries(V).forEach(([k,v])=>{{
    const b=document.createElement('button');
    b.className='cat-btn';b.dataset.cat=k;b.textContent=v.e+' '+v.name;
    b.addEventListener('click',()=>selCat(k,b));
    row.appendChild(b);
  }});
  updateWC();
}})();
function selCat(cat,btn){{
  document.querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('sel'));
  btn.classList.add('sel');S.cat=cat;updateWC();
}}
function updateWC(){{document.getElementById('wcount').textContent='共 '+getWords(S.cat).length+' 個單字'}}
document.querySelectorAll('.mode-card').forEach(c=>{{c.addEventListener('click',()=>{{S.mode=c.dataset.mode;S.words=shuffle(getWords(S.cat));startGame()}})}}); 
function startGame(){{if(S.mode==='flashcard')startFC();else if(S.mode==='quiz')startQuiz();else if(S.mode==='spell')startSpell();else if(S.mode==='match')startMatch()}}
function restart(){{S.words=shuffle(getWords(S.cat));startGame()}}
let FC={{idx:0,learned:0,flipped:false}};
function startFC(){{FC={{idx:0,learned:0,flipped:false}};showScr('flashcard');renderFC()}}
function renderFC(){{
  const tot=S.words.length;if(FC.idx>=tot){{showResults('flashcard',FC.learned,tot);return}}
  const w=S.words[FC.idx];FC.flipped=false;
  const el=document.getElementById('fc');el.style.transition='none';el.classList.remove('flipped');
  setTimeout(()=>{{el.style.transition=''}},50);
  document.getElementById('fc-btns').classList.add('hidden');
  document.getElementById('fc-emo').textContent=w.e;document.getElementById('fc-emo2').textContent=w.e;
  document.getElementById('fc-word').textContent=w.en;document.getElementById('fc-word2').textContent=w.en;
  document.getElementById('fc-zh').textContent=w.zh;document.getElementById('fc-cat').textContent=getCat(w.en);
  document.getElementById('fc-score').textContent='✅ '+FC.learned;
  const p=(FC.idx/tot)*100;
  document.getElementById('fc-prog').style.width=p+'%';document.getElementById('fc-ptxt').textContent='第 '+(FC.idx+1)+' / '+tot+' 張';
}}
function flipCard(){{if(FC.flipped)return;FC.flipped=true;document.getElementById('fc').classList.add('flipped');document.getElementById('fc-btns').classList.remove('hidden')}}
function fcAct(a){{if(a==='learned')FC.learned++;FC.idx++;renderFC()}}
let QZ={{words:[],idx:0,score:0,dir:'zh2en',answered:false,correctIdx:0,curWord:null}};
let qzCurOpts=[];
function startQuiz(){{QZ.words=shuffle(S.words).slice(0,Math.min(20,S.words.length));QZ.idx=0;QZ.score=0;QZ.answered=false;showScr('quiz');renderQuiz()}}
function setDir(d){{QZ.dir=d;document.getElementById('d-zh').classList.toggle('active',d==='zh2en');document.getElementById('d-en').classList.toggle('active',d==='en2zh');QZ.words=shuffle(S.words).slice(0,Math.min(20,S.words.length));QZ.idx=0;QZ.score=0;QZ.answered=false;renderQuiz()}}
function speakQW(){{if(QZ.curWord)speak(QZ.curWord.en)}}
function renderQuiz(){{
  const tot=QZ.words.length;if(QZ.idx>=tot){{showResults('quiz',QZ.score,tot);return}}
  QZ.answered=false;const w=QZ.words[QZ.idx];QZ.curWord=w;
  const all=getWords(S.cat);const others=shuffle(all.filter(x=>x.en!==w.en)).slice(0,3);
  const opts=shuffle([w,...others]);qzCurOpts=opts;
  QZ.correctIdx=opts.findIndex(o=>o.en===w.en);
  const isZH=QZ.dir==='zh2en';
  document.getElementById('q-emo').textContent=w.e;
  document.getElementById('q-word').textContent=isZH?w.zh:w.en;
  document.getElementById('q-lbl').textContent=isZH?'這個中文是什麼英文？':'這個英文是什麼意思？';
  const spkBtn=document.getElementById('q-speak-btn');spkBtn.style.display=isZH?'none':'inline';
  const btns=document.querySelectorAll('.quiz-opt');
  opts.forEach((opt,i)=>{{btns[i].textContent=isZH?opt.en:opt.zh;btns[i].className='quiz-opt';btns[i].disabled=false;btns[i].onclick=()=>checkQuiz(i)}});
  document.getElementById('q-score').textContent='⭐ '+QZ.score;
  const p=(QZ.idx/tot)*100;document.getElementById('q-prog').style.width=p+'%';document.getElementById('q-ptxt').textContent='第 '+(QZ.idx+1)+' / '+tot+' 題';
}}
function checkQuiz(i){{
  if(QZ.answered)return;QZ.answered=true;
  const btns=document.querySelectorAll('.quiz-opt');btns.forEach(b=>b.disabled=true);
  if(i===QZ.correctIdx){{btns[i].classList.add('correct');QZ.score++}}
  else{{btns[i].classList.add('wrong');btns[QZ.correctIdx].classList.add('correct')}}
  document.getElementById('q-score').textContent='⭐ '+QZ.score;
  setTimeout(()=>{{QZ.idx++;renderQuiz()}},1300);
}}
let SP={{words:[],idx:0,score:0,answered:false,hints:0}};
function startSpell(){{SP.words=shuffle(S.words).slice(0,Math.min(20,S.words.length));SP.idx=0;SP.score=0;SP.answered=false;SP.hints=0;showScr('spell');renderSpell()}}
function renderSpell(){{
  const tot=SP.words.length;if(SP.idx>=tot){{showResults('spell',SP.score,tot);return}}
  SP.answered=false;SP.hints=0;const w=SP.words[SP.idx];
  document.getElementById('sp-emo').textContent=w.e;document.getElementById('sp-zh').textContent=w.zh;
  const inp=document.getElementById('sp-inp');inp.value='';inp.className='spell-input';inp.disabled=false;inp.placeholder='輸入英文...';
  setTimeout(()=>inp.focus(),200);
  const fb=document.getElementById('sp-fb');fb.className='spell-feedback';fb.textContent='';
  document.getElementById('sp-next').className='btn-next-spell';
  document.getElementById('sp-score').textContent='⭐ '+SP.score;
  const p=(SP.idx/tot)*100;document.getElementById('sp-prog').style.width=p+'%';document.getElementById('sp-ptxt').textContent='第 '+(SP.idx+1)+' / '+tot+' 題';
}}
function spHint(){{if(SP.answered)return;const w=SP.words[SP.idx];const inp=document.getElementById('sp-inp');SP.hints++;const show=Math.min(SP.hints*2,w.en.length-1);inp.value=w.en.substring(0,show);inp.focus()}}
function checkSpell(){{
  if(SP.answered)return;const w=SP.words[SP.idx];const inp=document.getElementById('sp-inp');const ans=inp.value.trim().toLowerCase();if(!ans)return;
  SP.answered=true;inp.disabled=true;const fb=document.getElementById('sp-fb');
  if(ans===w.en.toLowerCase()){{inp.className='spell-input correct';fb.className='spell-feedback ok';fb.textContent='🎉 正確！ '+w.en+' = '+w.zh;SP.score++}}
  else{{inp.className='spell-input wrong';fb.className='spell-feedback no';fb.textContent='❌ 正確答案是：'+w.en}}
  document.getElementById('sp-score').textContent='⭐ '+SP.score;
  document.getElementById('sp-next').className='btn-next-spell show';
}}
function nextSpell(){{SP.idx++;renderSpell()}}
document.getElementById('sp-inp').addEventListener('keydown',e=>{{if(e.key==='Enter'){{if(!SP.answered)checkSpell();else nextSpell()}}}});
let MT={{sets:[],round:0,totalRounds:0,matched:0,sel:null,selEl:null,score:0,wrongs:0}};
function startMatch(){{
  const all=shuffle(S.words);MT.sets=[];
  for(let i=0;i<all.length;i+=4)MT.sets.push(all.slice(i,Math.min(i+4,all.length)));
  if(MT.sets.length>1&&MT.sets[MT.sets.length-1].length<2)MT.sets.pop();
  MT.round=0;MT.totalRounds=MT.sets.length;MT.score=0;MT.wrongs=0;showScr('match');renderMatchRound();
}}
function renderMatchRound(){{
  if(MT.round>=MT.totalRounds){{showResults('match',MT.score,MT.sets.reduce((s,a)=>s+a.length,0));return}}
  const set=MT.sets[MT.round];MT.matched=0;MT.sel=null;MT.selEl=null;
  const enOrd=shuffle([...Array(set.length).keys()]);const zhOrd=shuffle([...Array(set.length).keys()]);
  const grid=document.getElementById('mt-grid');grid.innerHTML='';
  for(let i=0;i<set.length;i++){{
    const ew=set[enOrd[i]],zw=set[zhOrd[i]];
    grid.appendChild(makeTile(ew.en,'en',enOrd[i]));grid.appendChild(makeTile(zw.zh,'zh',zhOrd[i]));
  }}
  const tot=MT.totalRounds;
  document.getElementById('mt-prog').style.width=(MT.round/tot*100)+'%';
  document.getElementById('mt-ptxt').textContent='第 '+(MT.round+1)+' / '+tot+' 輪';
  document.getElementById('mt-score').textContent='✅ 0/'+set.length;
}}
function makeTile(txt,type,idx){{const t=document.createElement('div');t.className='m-tile';t.dataset.type=type;t.dataset.idx=idx;t.textContent=txt;t.addEventListener('click',()=>onTile(t));return t}}
function onTile(t){{
  if(t.classList.contains('matched'))return;
  if(t===MT.selEl){{t.classList.remove('sel');MT.sel=null;MT.selEl=null;return}}
  if(!MT.sel){{t.classList.add('sel');MT.sel={{type:t.dataset.type,idx:+t.dataset.idx}};MT.selEl=t}}
  else{{
    const cur={{type:t.dataset.type,idx:+t.dataset.idx}};
    if(MT.sel.type===cur.type){{MT.selEl.classList.remove('sel');t.classList.add('sel');MT.sel=cur;MT.selEl=t;return}}
    if(MT.sel.idx===cur.idx){{
      MT.selEl.classList.remove('sel');MT.selEl.classList.add('matched');t.classList.add('matched');
      MT.sel=null;MT.selEl=null;MT.matched++;MT.score++;
      const setLen=MT.sets[MT.round].length;document.getElementById('mt-score').textContent='✅ '+MT.matched+'/'+setLen;
      if(MT.matched>=setLen)setTimeout(()=>{{MT.round++;renderMatchRound()}},700);
    }}else{{
      MT.wrongs++;const prev=MT.selEl;MT.selEl.classList.remove('sel');
      [prev,t].forEach(el=>{{el.classList.add('shake','wrong-fl');setTimeout(()=>el.classList.remove('shake','wrong-fl'),500)}});
      MT.sel=null;MT.selEl=null;
    }}
  }}
}}
function showResults(mode,score,total){{
  const pct=score/total;let ico,title,sub,stars,lbl='答對題數';
  if(mode==='flashcard'){{ico='📖';title='複習完成！';sub='你翻完了全部單字！';lbl='記住了幾個';stars=pct>=0.8?'⭐⭐⭐':pct>=0.5?'⭐⭐':'⭐'}}
  else if(mode==='match'){{ico=MT.wrongs===0?'🏆':'🧩';title=MT.wrongs===0?'完美配對！':'配對完成！';sub=MT.wrongs===0?'一次全對！':'錯了 '+MT.wrongs+' 次，再練！';lbl='配對正確數';stars=MT.wrongs===0?'⭐⭐⭐':MT.wrongs<=3?'⭐⭐':'⭐'}}
  else{{if(pct===1){{ico='🏆';title='滿分！超級棒！';sub='你全部都答對了！';stars='⭐⭐⭐'}}else if(pct>=0.8){{ico='🎉';title='太棒了！';sub='繼續保持！';stars='⭐⭐⭐'}}else if(pct>=0.6){{ico='😊';title='很不錯！';sub='再練一下更好！';stars='⭐⭐'}}else{{ico='💪';title='加油！';sub='多練習幾次就會更好！';stars='⭐'}}}}
  document.getElementById('res-ico').textContent=ico;document.getElementById('res-title').textContent=title;
  document.getElementById('res-sub').textContent=sub;document.getElementById('res-num').textContent=score+' / '+total;
  document.getElementById('res-lbl').textContent=lbl;document.getElementById('res-stars').textContent=stars;showScr('results');
}}
</script>
</body>
</html>'''

BG_COLORS = {
  "week2": ("#FFF9C4","#FCE4EC","#E3F2FD"),
  "week3": ("#E8F5E9","#FFF3E0","#E3F2FD"),
  "week4": ("#EDE7F6","#FCE4EC","#E8F5E9"),
  "week5": ("#FFF9C4","#E8EAF6","#FCE4EC"),
  "week6": ("#E0F7FA","#FFF9C4","#E8F5E9"),
  "week7": ("#FFF3E0","#E3F2FD","#FCE4EC"),
  "week8": ("#E8EAF6","#FFF9C4","#E0F7FA"),
}

for week_key, wdata in WEEKS.items():
    v_obj = make_v_obj(wdata["cats"])
    bg = BG_COLORS[week_key]
    html = HTML_TEMPLATE.format(
        title=wdata["title"],
        subtitle=wdata["subtitle"],
        V_OBJ=v_obj,
        bg1=bg[0], bg2=bg[1], bg3=bg[2],
    )
    fname = os.path.join(OUT, f"{week_key}_vocab.html")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {fname} ({len(html):,} bytes)")

print("All done!")
