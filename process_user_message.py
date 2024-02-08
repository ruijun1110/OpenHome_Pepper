from capabilities.capabilities_manager import check_and_perform_action
def process_message(message):
    """
    This function takes user message and processes it to figure out the event to trigger.
    It returns events flags and message vaidity flag.
    Validity means is message empty or not.


    Args:
        message (string): String message of user generated from speech to text openai service.

    Returns:
        exit_flag (Boolean): A boolean flag to know stop the process or not.
        is_valid_message (Boolean): A boolean flag to know if user has spoken something or not.
    """
    check_and_perform_action(message)
    
    # assuming user message is valid
    is_valid_message = True
    # check if user message have some thing in it.
    if message in ['.', '']:
        is_valid_message = False
    return is_valid_message