from datetime import timedelta

# Returns delay until next repetition based on stage
def next_interval(stage: int) -> timedelta:
    if stage == 1:
        return timedelta(minutes=25)
    elif stage == 2:
        return timedelta(days=1)
    elif stage == 3:
        return timedelta(weeks=2)
    elif stage == 4:
        return timedelta(weeks=8)
    else:
        return timedelta(days=0)
