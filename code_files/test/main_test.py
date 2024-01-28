import timeit
import pandas as pd
import numpy as np
from country_test import Abroad

# start timer
start_time = timeit.default_timer()


courses = ['commerce', 'aviation']

try:
    
    data_frames = {}

    for course in courses:
        
        # make an object------
        data = Abroad(course)

        # access the method-------
        data.city()
        
        info = {
            "Universities Names":data.university_name,
            "University Place":data.university_place,
            "Tuition Fess":data.tuition_fees,
            "Living Fees":data.living_fees,
            "Ratings out of 10":data.ratings
            }
        
        df = pd.DataFrame.from_dict(info, orient='index')
        df = df.transpose()
        df.index = np.arange(1, len(df) + 1)
        df["Rank"] = np.arange(1, len(df) + 1)

        data_frames[course] = df


    for key, data_frame in data_frames.items():
        print()
        print(f'Course : {key}')
        print(data_frame)
        print()


except Exception as e:
    print(e)


# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")