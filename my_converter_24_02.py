import random
import nltk  # edit_distance how dissimilar two strings (e.g., words) are
import json
import numpy as np
import pickle
import requests
from bs4 import BeautifulSoup
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)




def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def btcusd_command(update: Update, context: CallbackContext) -> None:
    url = 'https://www.rbc.ru/crypto/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    btcusd_parsed = soup.find('div', class_ = 'currencies__list js-index-currencies-list').find('a', class_ = 'currencies__item js-index-currencies-item').findAll('span', class_ = 'currencies__td__inner')[1].text.replace(',', '.').replace(' ','')
    btcusd = float(btcusd_parsed)
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(context.args[0]) + ' btc is ' + str(float(context.args[0].replace(',', '.')) * btcusd) + ' usd')

def xrpusd_command(update: Update, context: CallbackContext) -> None:
    url = 'https://www.rbc.ru/crypto/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    xrpusd_parsed = soup.find('div', class_ = 'currencies__list js-index-currencies-list').findAll('a', class_ = 'currencies__item js-index-currencies-item')[1].findAll('span', class_ = 'currencies__td__inner')[1].text.replace(',', '.')
    xrpusd = float(xrpusd_parsed)
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(context.args[0]) + ' xrp is ' + str(float(context.args[0].replace(',', '.')) * xrpusd) + ' usd')
def ethusd_command(update: Update, context: CallbackContext) -> None:
    url = 'https://www.rbc.ru/crypto/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    ethusd_parsed = soup.find('div', class_ = 'currencies__list js-index-currencies-list').findAll('a', class_ = 'currencies__item js-index-currencies-item')[2].findAll('span', class_ = 'currencies__td__inner')[1].text.replace(',', '.').replace(' ','')
    ethusd = float(ethusd_parsed)
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(context.args[0]) + ' eth is ' + str(float(context.args[0].replace(',', '.')) * ethusd) + ' usd')

def ltcusd_command(update: Update, context: CallbackContext) -> None:
    url = 'https://www.rbc.ru/crypto/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    ltcusd_parsed = soup.find('div', class_ = 'currencies__list js-index-currencies-list').findAll('a', class_ = 'currencies__item js-index-currencies-item')[3].findAll('span', class_ = 'currencies__td__inner')[1].text.replace(',', '.').replace(' ','')
    ltcusd = float(ltcusd_parsed)
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(context.args[0]) + ' ltc is ' + str(float(context.args[0].replace(',', '.')) * ltcusd) + ' usd')
'''''
def rubsat_command(update: Update, context: CallbackContext) -> None:
    url = 'https://www.rbc.ru/crypto/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    btcusd_parsed = soup.find('div', class_ = 'currencies__list js-index-currencies-list').find('a', class_ = 'currencies__item js-index-currencies-item').findAll('span', class_ = 'currencies__td__inner')[1].text.replace(',', '.').replace(' ','')
    btcusd = float(btcusd_parsed)
    context.bot.send_message(chat_id=update.effective_chat.id, text= str(context.args[0]) + ' rub is ' + str(float(context.args[0].replace(',', '.')) * btcusd) + ' usd')
'''''





def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5173253568:AAHEjjZZirduy_FJ9vdDO2R1G4fQsFBKc1o")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("btcusd", btcusd_command))
    dispatcher.add_handler(CommandHandler("ethusd", ethusd_command))
    dispatcher.add_handler(CommandHandler("xrpusd", xrpusd_command))
    dispatcher.add_handler(CommandHandler("ltcusd", ltcusd_command))






   
    ''''
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    '''''


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

