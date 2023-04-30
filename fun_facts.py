def print_fun_fact(name):
    fun_facts = {
        "Abubakar": "Abdulsalami Abubakar once won a national squash tournament in Nigeria.",
        "Obasanjo": "Olusegun Obasanjo has a black belt in karate.",
        "Yar'Adua": "Umaru Musa Yar'Adua was a talented painter and sold some of his artworks to support himself while he was a university student.",
        "Jonathan": "Goodluck Jonathan is a big fan of Nollywood movies and has appeared in a few of them as an extra.",
        "Buhari": "Muhammadu Buhari used to work as a professional wrestler before joining the military.",
        "Shonekan": "Ernest Shonekan is a skilled pianist and once performed at a state banquet in Nigeria.",
        "Abacha": "Sani Abacha was a fan of extreme sports and once went skydiving in the United States.",
        "Babangida": "Ibrahim Babangida is an accomplished poet and has published several collections of his poems.",
        "Shagari": "Shehu Shagari used to be a fashion model in his youth and once walked the runway at a fashion show in Lagos.",
        "Gowon": "Yakubu Gowon is a polyglot and can speak over ten languages fluently.",
    }

    if name in fun_facts:
        # ANSI escape sequence for yellow color
        yellow = '\033[93m'
        # ANSI escape sequence for resetting color
        reset = '\033[0m'
        print(f"{yellow}Here's a fun fact about {name}:{reset}\n{fun_facts[name]}")
    else:
        # ANSI escape sequence for red color
        red = '\033[91m'
        # ANSI escape sequence for blue color
        blue = '\033[94m'
        # ANSI escape sequence for resetting color
        reset = '\033[0m'
        print(f"{red}Sorry, I don't have a fun fact about {name}.{reset}")
        name = input(f"{blue}Enter a last name of a former Nigerian President: {reset}")
        print_fun_fact(name.title())


# Initial input prompt
name = input("\033[94mEnter a last name of a former Nigerian President: \033[0m")
print_fun_fact(name.title())
