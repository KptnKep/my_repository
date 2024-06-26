import json
import random
import time
import base64

c = [{
    "key": str(1),
    "descr": "Pos. " + str(1),
    "string1": "Воробей",
    "string2": "Серый"
    },
    {
    "key": str(2),
    "descr": "Pos. " + str(2),
    "string1": "Сорока",
    "string2": "черно-белый"
    },
    {
    "key": str(3),
    "descr": "Pos. " + str(3),
    "string1": "Ворона",
    "string2": "Серый"
    },
    {
    "key": str(4),
    "descr": "Pos. " + str(4),
    "string1": "Воробей",
    "string2": "Серый"
    }]


def new_window_on_open(hashMap, _files=None, _data=None):
    hashMap.put("ShowScreen", "Экран2")
    return hashMap


def customcards_on_open(hashMap, _files=None, _data=None):
    j = {"customcards": {

        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "Picture",
                            "show_by_condition": "",
                            "Value": "@pic1",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        },
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string1",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string2",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string3",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                }
                                ,
                                {
                                    "type": "LinearLayout",
                                    "orientation": "horizontal",
                                    "height": "wrap_content",
                                    "width": "match_parent",
                                    "weight": "1",
                                    "Elements": [
                                        {
                                            "type": "Button",
                                            "Value": "&#xf1de;",
                                            "Variable": "btn_plus",
                                            "style_class": "beautiful_button"
                                        },
                                        {
                                            "type": "Button",
                                            "Value": "&#xf044;",
                                            "Variable": "btn_minus",
                                            "style_class": "beautiful_button"
                                        }

                                    ]}

                            ]
                        },
                        {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@val",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        }
                    ]
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@descr",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "-1",
                    "TextColor": "#6F9393",
                    "TextBold": False,
                    "TextItalic": True,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                }
            ]
        }

    }
    }

    j["customcards"]["cardsdata"] = c
    # for i in range(0,5):
    #     c =  {
    #     "key": str(i),
    #     "descr": "Pos. "+str(i),
    #     "val": str(random.randint(10, 10000))+" руб.",
    #     "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
    #     "string2": "Гнездо процессора LGA 1700",
    #     "string3": "Частотная спецификация памяти 4800 МГц"
    #   }
    #     j["customcards"]["cardsdata"].append(c)

    hashMap.put("cards", json.dumps(j, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def save_bird(hashMap, _files=None, _data=None):

    i = len(c) + 1
    data = {
        "key": str(i),
        "descr": "Pos. " + str(i),
        "string1": hashMap.get("bird"),
        "string2": hashMap.get("bloom")
    }

    c.append(data)
    hashMap.put("toast", "Добавленно" )


    return hashMap
