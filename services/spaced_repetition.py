from datetime import timedelta, datetime
import asyncio
from services.scheduler import send_scheduled_exercise, scheduler

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

def schedule_repetition(bot, user_id: int, word: str, learned_at: datetime = None):
    """
    Schedule spaced repetition exercises for a word.
    Stages 1–4 use next_interval delays from the learned_at timestamp.
    """
    base_time = learned_at or datetime.utcnow()
    for stage in range(1, 5):
        run_time = base_time + next_interval(stage)
        scheduler.add_job(
            lambda u=user_id, w=word: asyncio.create_task(send_scheduled_exercise(bot, u)),
            'date',
            run_date=run_time,
            id=f"repetition_{user_id}_{word}_{stage}"
        )
