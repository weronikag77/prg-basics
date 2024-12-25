# tv_show.py file
# main program
import tv

arr = ["1. TVP1","2. TVP2","3. Polsat","4. TVN","5. Filmbox","6. Discovery", "7. HBO"]
def main():
   my_tv = tv.TV()
   my_tv.turn_on()
   my_tv.set_channel(5)
   my_tv.volume_increase()
   my_tv.volume_increase()
   my_tv.volume_increase()
   my_tv.volume_increase()
   my_tv.volume_decrease()
   my_tv.volume_increase()
   my_tv.volume_decrease()
   my_tv.volume_decrease()
   my_tv.set_channels(arr)
   my_tv.show_status()



if __name__ =="__main__":
   main()

