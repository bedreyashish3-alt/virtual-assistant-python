from assistant import *

def execute_command(query):

    if query == "":
        return True

    if "open google" in query:
        open_google()

    elif "open youtube" in query:
        open_youtube()

    elif "open gmail" in query:
        open_gmail()

    elif "open instagram" in query:
        open_instagram()

    elif "wikipedia" in query:
        wikipedia_search(query)

    elif "search" in query:
        google_search(query)

    elif "play" in query:
        play_song(query)

    elif "joke" in query:
        tell_joke()

    elif "time" in query:
        tell_time()

    elif "date" in query:
        tell_date()

    elif "map" in query:
        open_map(query)

    elif "shutdown" in query:
        shutdown()

    elif "bye" in query or "exit" in query:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


def main():

    wish()

    while True:

        query = listen()

        if not execute_command(query):
            break


if __name__ == "__main__":
    main()