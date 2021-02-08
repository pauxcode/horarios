from datetime import datetime
import pytz

naive = datetime.now()
## Tzinfo is missing from the time object 
## which is naive 
print("Tzinfo:", naive.tzinfo)
print()

## After adding the timezone info, 
## the object it becomes aware
timezone = pytz.timezone("Asia/Tokyo")
aware2 = naive.astimezone(timezone)
#resta = naive - aware2

print("Initial tzinfo:",naive.tzinfo)
print("Final tzinfo:",aware2.tzinfo)
#print(resta)
print(naive)
print(aware2)
