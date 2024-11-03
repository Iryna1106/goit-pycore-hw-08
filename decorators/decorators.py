from functools import wraps
import colorama 


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{colorama.Fore.RED}Invalid command. Provide name and phone number.{colorama.Style.RESET_ALL}"
        except KeyError as e:
            return f"{colorama.Fore.RED}{e.args[0]}. Provide  name of an existing contact.{colorama.Style.RESET_ALL}"
        except IndexError:
            return f"{colorama.Fore.RED}Invalid command. Provide a valid contact name.{colorama.Style.RESET_ALL}"

    return inner