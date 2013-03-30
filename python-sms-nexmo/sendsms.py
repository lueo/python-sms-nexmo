# -*- coding: utf-8 -*-
"""Send you SMS in one line.

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

"""
from docopt import docopt
import sys, traceback

from libpynexmo.nexmomessage import NexmoMessage
from phonenumbers import PhoneNumber, NumberFormat, phonenumberutil
from schema import Schema, And, Use, Or, SchemaError
import ConfigParser
import logging

__version__ = '0.0.1a'

def main(args):

    if args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)

    logging.debug(args)

    schema = Schema({
        '--country': Schema(lambda c: c in phonenumberutil.SUPPORTED_REGIONS, error='Invalid country code'),
        'TO_NUM': basestring,
        'FROM_NUM': basestring,
        'MESSAGE': basestring,
        str: object
        })

    try:
        args = schema.validate(args)
    except SchemaError, e:
        logging.error(traceback.format_exc())
        exit(e)


    try:
        logging.debug('Parsing config files...')
        config = ConfigParser.RawConfigParser()
        config.read(args['--config'])
        api_key = config.get('Password', 'api_key')
        api_secret = config.get('Password', 'api_secret')
    except Exception, e:
        logging.error(traceback.format_exc())
        exit(e)

    msg = args['MESSAGE']
    f_num = args['FROM_NUM']
    t_num = args['TO_NUM']
    country = args['--country']
    if t_num[0] == '+':
        logging.debug('Senderid use E164 form, e.g. +886123456...')
        from_num = phonenumberutil.format_number(phonenumberutil.parse(f_num, country) \
                , phonenumberutil.PhoneNumberFormat.E164).lstrip('+')
    logging.debug('Senderid use national form, e.g. 09123456...')
    from_num = ''.join(phonenumberutil.format_number(phonenumberutil.parse(f_num, country) \
             , phonenumberutil.PhoneNumberFormat.NATIONAL).split())
    to_num = phonenumberutil.format_number(phonenumberutil.parse(t_num, country) \
            , phonenumberutil.PhoneNumberFormat.E164)

    sms = NexmoMessage({
            'reqtype': 'json',
            'type': 'unicode',
            'api_secret': api_secret,
            'api_key': api_key,
            'from': from_num,
            'to': to_num,
            'text': msg
          })
    logging.debug('details: %s' % sms.get_details())

    if not args['--dry']:
        res = sms.send_request()
        print 'finished, message detail: %s' % res
    else:
        print '==> dry run'

# def is_string_valid_phonenumber(num, ccode):
    # numobj = phonenumberutil.parse(num, ccode)
    # return phonenumberutil.is_valid_number(numobj)

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)

    main(args)

