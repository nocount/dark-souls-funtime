#Parsing weapon stats from CSV

#Libs
import pandas
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='Fr0ntranger')
cursor = conn.cursor()
cursor.execute('USE dark_souls')


cursor.execute('SELECT * FROM weapon_stats')
results = cursor.fetchall()
print(results)

df = pandas.read_csv('weapon_data.csv')

#Finding max damage numbers
mPhys = max(df['Physical'])
print("Highest base physical damage is: " + df['Name'][df['Physical'].idxmax()] + " at " + str(mPhys))

mMagic = max(df['Magic'])
print("Highest base magic damage is: " + df['Name'][df['Magic'].idxmax()] + " at " + str(mMagic))

mFire = max(df['Fire'])
print("Highest base fire damage is: " + df['Name'][df['Fire'].idxmax()] + " at " + str(mFire))

#Pretty sure this wont work with current formatting
mLightning = max(df['Lightning'])
print("Highest base lightning damage is: " + df['Name'][df['Lightning'].idxmax()] + " at " + str(mLightning))

#Highest total AR
mAR = max(df['Total AR'])
print("Highest total AR, ignoring split resists, is: " + df['Name'][df['Total AR'].idxmax()] + " at " + str(mAR))


print('\n')

#Showing top ten Highest AR
print("The top ten highest AR weapons:")
print(df.nlargest(10, 'Total AR'))

# sorted_df = df.sort_values(by=['Total AR'])

# for i in range(0,9):
# 	print(sorted_df[i])


