#Parsing weapon stats from CSV

#Libs
import pandas

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

mAR = max(df['Total AR'])
print("Highest total AR, ignoring split resists, is: " + df['Name'][df['Total AR'].idxmax()] + " at " + str(mAR))