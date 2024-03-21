package main

import (
    "log"
    "os"
    "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

func main() {
    // Get the Telegram bot token from environment variable
    botToken := os.Getenv("TELEGRAM_BOT_TOKEN")
    if botToken == "" {
        log.Fatal("Telegram bot token not found in environment variables")
    }

    // Create a new bot instance
    bot, err := tgbotapi.NewBotAPI(botToken)
    if err != nil {
        log.Fatal(err)
    }

    // Enable debugging to log HTTP requests
    bot.Debug = true

    log.Printf("Authorized on account %s", bot.Self.UserName)

    // Set up updates configuration
    updateConfig := tgbotapi.NewUpdate(0)
    updateConfig.Timeout = 60

    // Get updates from Telegram
    updates, err := bot.GetUpdatesChan(updateConfig)
    if err != nil {
        log.Fatal(err)
    }

    // Listen for incoming messages
    for update := range updates {
        if update.Message == nil { // ignore any non-Message Updates
            continue
        }

        // Log message details
        log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

        // Reply to the message
        reply := "Hello, I'm your bot!"
        msg := tgbotapi.NewMessage(update.Message.Chat.ID, reply)
        _, err := bot.Send(msg)
        if err != nil {
            log.Println("Error sending message:", err)
        }
    }
}
