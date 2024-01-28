import timeit
import pandas as pd
import numpy as np
from country_wise import Abroad

# start Timer
start_time = timeit.default_timer()

try:

    countries = ['canada', 'australia', 'germany', 'hong-kong', 'ireland', 'malaysia', 'netherlands', 
                'new-zealand', 'singapore', 'sweden', 'uk', 'usa', 'france', 'italy', 'uae']

    data_frames = {}

    for country in countries:
        # make an object------
        data = Abroad(country)

        # access the method-------
        data.city()
        
        try:
            info = {
                "Universities Names":data.university_name,
                "University Place":data.university_place,
                "Tuition Fess":data.tuition_fees,
                "Living Fees":data.living_fees
                }
            
            df = pd.DataFrame.from_dict(info, orient='index')
            df = df.transpose()
            df.index = np.arange(1, len(df) + 1)
            df["Rank"] = np.arange(1, len(df) + 1)

            data_frames[country] = df
            
        except Exception as e:
            print(e)



    excel_file = 'extracted_files/Country Wise Universities Data.xlsx'
        
    # Write each DataFrame to a different sheet in the same Excel file
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:

        for key, data_frame in data_frames.items():

            data_frame.to_excel(writer, sheet_name=key, index=False)



except Exception as e:
    print(e)

# end Timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")