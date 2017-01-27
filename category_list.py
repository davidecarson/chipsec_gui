# -*- coding: utf-8 -*-
categories = [
    {
        'name': u'تست های مربوط به متغیر های UEFI',
        'info': u"""تست حفاظت شدن از متغیر های UEFI، که در مشخصات UEFI، آمده 
        است و بررسی اینکه این متغیر ها مجوز های مشخصی داشته باشند.""",
        'modules': [
            'common.uefi.access_uefispc',
        ]
    },
    {
        'name': u'بررسی آسیب پذیری رمز عبور BIOS/HDD از طریق کیبورد در BIOS',
        'info': u'',
        'modules': [
            '‫‪',
        ]
    },
    {
        'name': u"""بررسی آسیب پذیری رمز عبور قبل بوت (Pre-Boot) در بافر کیبورد BIOS""",
        'info': u'',
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u"""بررسی و اطمینان حاصل کردن از قفل بودن تنظیمات مربوط به رخداد های SMI""",
        'info': u'',
        'modules': [
            'common.bios_smi',
        ]
    },
    {
        'name': u'آزمودن مکانیزم های حفاظت از ناحیه BIOS در فلش',
        'info': u"""در فلش، BIOS می­تواند هم از طریق مد مدیریت سیستم حفاظت شود 
        و هم از طریق تنظیمات موجود در کنترلر SPI.
        برای مثال برای اینکه این تست و در مکانیزم دوم یعنی استفاده از تنظیمات 
        کنترلر SPI با موفقیت پاس شود ، می بایست رجیستر های P0  تا P4 که مربوط 
        به بازه ی حفاظتی SPI هستند، تمام ناحیه ی بایوس را پوشش دهند. و اگر داده 
        های مهم دیگر مثل NVRAM پوشش داده نشود ممکن آن ناحیه آسیب پذیر باشد و 
        مورد حمله واقع شود.""",
        'modules': [
            '‫‪',
        ]
    },
    {
        'name': u'آزمودن تنظیمات SMRR',
        'info': u""")System Management mode Range Registers( ها و فعال یا 
        Enable بودن یا تنظیم بودنشان""",
        'modules': [
            'common.smrr',
        ]
    },
    {
        'name': u'بررسی تنظیمات کنترلر SPI',
        'info': u"""که شامل بررسی قفل بودن رنجهای محافظت شده ی PR0-PR4 تا زمان 
        Reset است.که اگر قفل نباشند می بایست این رجیستر ها مجدد پروگرم شوند""",
        'modules': [
            'common.spi_lock',
        ]
    },
    {
        'name': u'بررسی هندلر های SMI برای تشخیص اسیب پذیری های مربوط به آدرس دهی',
        'info': u'',
        'modules': [
            'tools.smm.smm_ptr'
        ]
    },
    {
        'name': u'بررسی تست های مربوط به حفاظت DMA',
        'info': u"""این تست تنظیمات و قفل بودن بازه تنظیمات SMRAM را بررسی کرده 
        و از صحت حفاظت در برابر حملات DMA اطمینان حاصل می کند.\nدر واقع 
        همانطور که SMRAM میبایست از نرن فازار هایی که در CPU اجرا می شوند 
        در امان باشد، نیاز دارد تا از سخت افزار هایی که دسترسی مستقیم به DRAM 
        دارند )DMA( نیز محافظت شود. درواقع حفاظت از DMA، از طریق پروگرم 
        کردن ناحیه حفاظت SMRAM تنظیم می شود و اگر BIOS به درستی تنظیم نشده و 
        این تنظیمات را قفل نکرده باشد، لذا مخرب ها می توانند تنظیمات را مجدد 
        پروگرم کرده و ناحیه SMRAM را در معرض دسترسی DMA قرار دهند. و در نتیجه 
        اجازه دستکاری حافظه ای را دهند که می بایست حفاظت شود.""",
        'modules': [
            'modules.smm_dma'
        ]
    },
    {
        'name': u'بررسی محتویات ROM سفت افزار UEFI',
        'info': u"""از طریق مقایسه آن با لیست سیاهی که قبلا در فایلی برای آن 
        تعریف شده است. و اگر فایل ها یا Image ها ناسالم اند، می بایست 
        امضای شان در این فایل تعریف گردد تا در مقایسه و صحت Image فعلی درنظر 
        گرفته شوند""",
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u'تست خواندن و نوشتن در فلش SPI',
        'info': u"""زمانی که یک فایل Image از خواندن فلش SPI ایجاد شد، 
        میتوان با ابزار توسعه داده شده  این Image را پاس کرد و بخش های مختلف آن 
        شامل متغیر ها، فایل ها و... را آشکار نمود.""",
        'modules': [
            'utilcmd.decode_cmd',
            'utilcmd.uefi_cmd'
        ]
    },
    {
        'name': u'قابلیت دسترسی به حافظه فیزیک',
        'info': u'',
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u'دسترسی به جداول ACPI و دستکاری آنها',
        'info': u'',
        'modules': [
            '‫‪'
        ]
    }
]
