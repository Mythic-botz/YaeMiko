# Mikobot/void.py

# ⏳ Time formatter used across the bot
def get_readable_time(seconds: int) -> str:
    """Convert seconds into a readable time format: Days, Hours, Minutes, Seconds"""
    count = 0
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        if count < 2:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)

        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
        count += 1

    # Format into human-readable string
    readable_time = ""
    for i in range(len(time_list)):
        readable_time += str(time_list[i]) + time_suffix_list[i]
        if i < len(time_list) - 1:
            readable_time += ", "
    return readable_time[::-1]