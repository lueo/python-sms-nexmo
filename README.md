python-sms-nexmo
================

Send your SMS by nexmo in one line.

**tl;dr**

1. Get a [NEXMO](http://nexmo.com/, "Get a nexmo account") account and find your ``API_KEY`` and ``API_SECRET``

    ```bash
    echo "[Password]
    api_key = xxxxxx
    api_secret = xxxxxx" > smssend.cfg
    ```

2. Send SMS!

    ```bash
    # python sendsms.py <FROM>       <TO>         <MESSAGES>    
    $ python sendsms.py 0982-532-661 0917-878-979 "How are you?" 
    # useful options:
     --dry     Dry run
     --debug   Debug
     --country Country code. Default: TW
    ```

Usage
---

### Config files (required)

Default config file is ``smssend.cfg``.

**Warning!** This file is readable in plain text.

If you need to secure this file, please place it in a encrypted driver.

Then read it by specify ``--config`` option (or ``-c``).

For example:
```bash
$ python sendsms.py <FROM> <TO> <MESSAGE> --config "D:\enc\sms.cfg"
```
### Country code (optional)

If you omit the country code, the default country code is TW (Taiwan, ROC).

You can specify it by ``--country`` option (or ``-r``).

```bash
$ python sendsms.py <FROM> <TO> <MESSAGE> --country US
$ python sendsms.py <FROM> <TO> <MESSAGE> -r US
```

### Detail usage
```
Usage: 
    sendsms.py [options] FROM_NUM TO_NUM MESSAGE
    sendsms.py (-h | --help)
    sendsms.py --version

    The api key should be saved in smssend.cfg in the following format:
    
    [Password]
    api_key = xxxxxx
    api_secret = xxxxxx

Arguments:
    FROM_NUM    Phone numbers to send message from 
    TO_NUM      Phone numbers to send message to 
    MESSAGE     Message to send message

Options:
    -h, --help  Show help message
    --version  Show version info.
    -r, --country=COUNTRY  Country in code [default: TW]
    -c, --config=CONFIG  Config file path [default: smssend.cfg]
    -d, --debug  Debug info
    --dry  Dry run
```

Installation
---
1. install virtualenv(optional)
2. ``$ git clone git://github.com/lueo/python-sms-nexmo.git``
3. ``$ cd python-sms-nexmo``
4. ``$ pip install -r requirements.txt``
5. Get a [NEXMO](http://nexmo.com/, "Get a nexmo account") account and find your ``API_KEY`` and ``API_SECRET``
6. Prepare a config file, named as "smssend.cfg"

```
[Password]
api_key = xxxxxx
api_secret = xxxxxx
```

Then send SMS by executing:
```bash
$ python sendsms.py FROM TO MESSAGE
```

Requirements
---

1. [docopt](https://github.com/docopt/docopt)
2. [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
3. [schema](https://github.com/halst/schema)

Motivation
---

Nexmo is the **MOST** excellent SMS service in the earth.

However, there are no excellent one-liner to send SMS by nexmo, what a shame...

So I made this one.

License
---

GPL v3. See [License](http://github.com/lueo/python-sms-nexmo/tree/master/LICENSE)

Thanks
---
[libpynexmo on github](https://github.com/marcuz/libpynexmo)
