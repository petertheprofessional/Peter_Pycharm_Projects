from tv import tv

if __name__ == '__main__':
    tv = tv()
    #turn on tv
    print(tv.turn_on())
    #Set the channel to 3
    tv.channel_up()
    tv.channel_up()
    #set the volume to 7
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    #turn off tv
    print(tv.turn_off())
    #turn tv back on
    print(tv.turn_on())
    channel = int(input("Select Channel"))
    tv.set_channel(channel)
    tv.volume_down()
    tv.volume_down()






