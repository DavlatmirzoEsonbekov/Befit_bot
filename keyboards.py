from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



# Universal "Ortga" tugmasi
back_button = KeyboardButton(text="🔙 Ortga")

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Befit Pro")],   # 1-qatorda 1 ta tugma
    [KeyboardButton(text="Befit Sky")]], # 2-qatorda 2 ta tugma  
    resize_keyboard=True)   # menu o'lchamini normallashtiradigan kod


main_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Befit Pro")],
    [KeyboardButton(text="Befit Sky")]
    
],resize_keyboard=True)





report_or_problem =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Hisobot"),KeyboardButton(text="Muammo")],
    [KeyboardButton(text="Asosiy menu")]], resize_keyboard=True)

sky_rep_to_prob = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Hisobot sky"),KeyboardButton(text="Muammo sky")],
    [KeyboardButton(text="Asosiy menu")]], resize_keyboard=True)

Pro_floor =ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text="-1"),KeyboardButton(text="1"),KeyboardButton(text="2")],
    [ KeyboardButton(text="3"),KeyboardButton(text="4")],
    [KeyboardButton(text="Ko'cha"), KeyboardButton(text="Basseyn")],
    [ KeyboardButton(text="Ortga")]

], resize_keyboard= True)
Pro_floor_problem =ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text="-1"),KeyboardButton(text="1"),KeyboardButton(text="2")],
    [ KeyboardButton(text="3"),KeyboardButton(text="4")],
    [KeyboardButton(text="Ko'cha"), KeyboardButton(text="Basseyn")],
    [ KeyboardButton(text="Ortga")]

], resize_keyboard= True)


# =============InlineKeyboard=========================

inline_buttons = {
        "-1": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Zona Spa", callback_data="zone_Spa")],
                                                    [InlineKeyboardButton(text="Sklad", callback_data="zone_Sklad")],
                                                    [InlineKeyboardButton(text = "Reception",callback_data="zone_Spa_reception")],
                                                    [InlineKeyboardButton(text="Shit", callback_data="zone_Shit")],
                                                    [InlineKeyboardButton(text="Sauna", callback_data="zone_Sauna")],
                                                    [InlineKeyboardButton(text="Basseyn", callback_data="zone_Basseyn")]
                                                    ]),
        "1": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Reception", callback_data="zone_Reception")],
                                                   [InlineKeyboardButton(text="Kiyinish xonasi E.", callback_data="zone_Razdevalka.E")],
                                                   [InlineKeyboardButton(text="Kiyinish xonasi A.", callback_data="zone_Razdevalka.A")],
                                                   [InlineKeyboardButton(text="Skladrom", callback_data="zone_Skladrom")],
                                                   [InlineKeyboardButton(text="Sotuv bo'limi", callback_data="zone_Sotuv_bo'limi")],
                                                   [InlineKeyboardButton(text="Bar", callback_data="zone_Bar")]
                                                   ]),
        "2": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Reception", callback_data="zone_Reception")],
                                                   [InlineKeyboardButton(text="Zona Fight", callback_data="zone_Fight")],
                                                   [InlineKeyboardButton(text="Crossfit", callback_data="zone_Crossfit")],
                                                   [InlineKeyboardButton(text="Trenerlar xonasi", callback_data="zone_Trener_xonasi")],
                                                   [InlineKeyboardButton(text="Medical room", callback_data="zone_Medical")]]),

        "3": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Reception", callback_data="zone_Reception")],
                                                   [InlineKeyboardButton(text="Zona Funksional", callback_data="zone_Funksional")],
                                                   [InlineKeyboardButton(text="Gym oldi", callback_data="zone_Gym_oldi")],
                                                   [InlineKeyboardButton(text="Gym orqa", callback_data="zone_Gym_orqa")],
                                                   [InlineKeyboardButton(text="Trenerlar xonasi", callback_data="zone_Trener_xonasi")]
                                                   ]),
        "4": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Cycling", callback_data="zone_Cycle")],
                                                   [InlineKeyboardButton(text="Body & Mind", callback_data="zone_Body_Mind")],
                                                   [InlineKeyboardButton(text="Zona Fitness", callback_data="zone_Fitness")],
                                                   [InlineKeyboardButton(text="Zona Meeting", callback_data="zone_Meeting")],
                                                   [InlineKeyboardButton(text="Zona Coffe", callback_data="zone_Kofe")]
                                                   ]),
        "Basseyn": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Reception", callback_data="zone_Reception_basseyn")],
                                                         [InlineKeyboardButton(text="Kiyinish xonasi E.", callback_data="zone_Razdevalka.E")],
                                                         [InlineKeyboardButton(text="Kiyinish xonasi A.", callback_data="zone_Razdevalka.A")],
                                                         [InlineKeyboardButton(text="Tribuna", callback_data="zone_Tribuna")]
                                                    ]),
        "Ko'cha": InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Asosiy kirish", callback_data="zone_Asosiy_kirish")],
                                                        [InlineKeyboardButton(text="Katelniy", callback_data="zone_Katelniy")],
                                                        [InlineKeyboardButton(text="Worcout", callback_data="zone_Worcout")],
                                                        [InlineKeyboardButton(text="Moyka", callback_data="zone_Moyka")]

        ])                                                                                       
    }


