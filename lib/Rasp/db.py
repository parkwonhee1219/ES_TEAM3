import MySQLdb

db_sensors = MySQLdb.connect("localhost", "pwh1219", "1219", "week_5")

# aircon
def insert_aircon_info(aircon):
    cur = db_sensors.cursor()
    if (aircon == 1):
        state = "ON"
    else:
        state = "OFF"
    insert_db = '''
        insert into aircon (state) values (%s)
    '''

    cur.execute(insert_db, (state, ))
    db_sensors.commit()
    cur.close()

def print_aircon_db(last = None):
    cur = db_sensors.cursor()

    if (last == None):
        print_db = '''
            select * from aircon
        '''
        cur.execute(print_db)
        while (True):
            temp = cur.fetchone()
            if not temp: break
            print("aircon state: {}, time: {}".format(temp[0], temp[1]))
    else:
        print_db = '''
            select state, dt FROM aircon
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(print_db)
        temp = cur.fetchone()
        print("aircon state: {}, time: {}".format(temp[0], temp[1]))
    cur.close()

def delete_aircon_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from aircon
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from aircon
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(delete_db)
        
    db_sensors.commit()
    cur.close()

# heater
def insert_heater_info(heater):
    cur = db_sensors.cursor()
    if (heater == 1):
        state = "ON"
    else:
        state = "OFF"
    insert_db = '''
        insert into heater (state) values (%s)
    '''

    cur.execute(insert_db, (state, ))
    db_sensors.commit()
    cur.close()

def print_heater_db(last = None):
    cur = db_sensors.cursor()

    if (last == None):
        print_db = '''
            select * from heater
        '''
        cur.execute(print_db)
        while (True):
            temp = cur.fetchone()
            if not temp: break
            print("heater state: {}, time: {}".format(temp[0], temp[1]))
    else:
        print_db = '''
            select state, dt FROM heater
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(print_db)
        temp = cur.fetchone()
        print("heater state: {}, time: {}".format(temp[0], temp[1]))
    cur.close()

def delete_heater_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from heater
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from heater
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(delete_db)
        
    db_sensors.commit()
    cur.close()

# dehumidifier
def insert_dehumidifier_info(dehumid):
    cur = db_sensors.cursor()
    if (dehumid == 1):
        state = "ON"
    else:
        state = "OFF"
    insert_db = '''
        insert into dehumidifier (state) values (%s)
    '''

    cur.execute(insert_db, (state, ))
    db_sensors.commit()
    cur.close()

def print_dehumidifier_db(last = None):
    cur = db_sensors.cursor()

    if (last == None):
        print_db = '''
            select * from dehumidifier
        '''
        cur.execute(print_db)
        while (True):
            temp = cur.fetchone()
            if not temp: break
            print("dehumidifier state: {}, time: {}".format(temp[0], temp[1]))
    else:
        print_db = '''
            select state, dt FROM dehumidifier
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(print_db)
        temp = cur.fetchone()
        print("dehumidifier state: {}, time: {}".format(temp[0], temp[1]))
    cur.close()

def delete_dehumidifier_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from dehumidifier
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from dehumidifier
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(delete_db)
        
    db_sensors.commit()
    cur.close()

#-----------------------------------------------------------------

# temperature
def insert_temperature_info(temp):
    cur = db_sensors.cursor()
    insert_db = '''
        insert into temperature (temp) values (%s)
    '''

    cur.execute(insert_db, (temp, ))
    db_sensors.commit()
    cur.close()

def print_temperature_db():
    cur = db_sensors.cursor()
    print_db = '''
        select * from temperature
    '''
    cur.execute(print_db)
    while (True):
        temp = cur.fetchone()
        if not temp: break
        print("temperature: ", temp[1])
    
    cur.close()

def delete_temperature_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from temperature
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from temperature WHERE temp = %s
        '''
        cur.execute(delete_db, (value, ))
        
    db_sensors.commit()
    cur.close()

# humidity
def insert_humidity_info(humid):
    cur = db_sensors.cursor()
    insert_db = '''
        insert into humidity (humid) values (%s)
    '''

    cur.execute(insert_db, (humid, ))
    db_sensors.commit()
    cur.close()

def print_humidity_db():
    cur = db_sensors.cursor()
    print_db = '''
        select * from humidity
    '''
    cur.execute(print_db)
    while (True):
        humid = cur.fetchone()
        if not humid: break
        print("humidity: ", humid[1])
    
    cur.close()

def delete_humidity_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from humidity
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from humidity WHERE humid = %s
        '''
        cur.execute(delete_db, (value, ))
        
    db_sensors.commit()
    cur.close()

# distance
def insert_distance_info(dist):
    cur = db_sensors.cursor()
    insert_db = '''
        insert into distance (dist) values (%s)
    '''

    cur.execute(insert_db, (dist, ))
    db_sensors.commit()
    cur.close()

def print_distance_db():
    cur = db_sensors.cursor()
    print_db = '''
        select * from distance
    '''
    cur.execute(print_db)
    while (True):
        dist = cur.fetchone()
        if not dist: break
        print("distance: ", dist[1])
    
    cur.close()

def delete_distance_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from distance
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from distance WHERE dist = %s
        '''
        cur.execute(delete_db, (value, ))
        
    db_sensors.commit()
    cur.close()

# touch
def insert_touch_info(state):
    # if (state == 1):
    #     value = "ON"
    # else:
    #     value = "OFF"
    cur = db_sensors.cursor()
    insert_db = '''
        insert into touch (state) values (%s)
    '''

    cur.execute(insert_db, (state, ))
    db_sensors.commit()
    cur.close()

def print_touch_db():
    cur = db_sensors.cursor()
    print_db = '''
        select * from touch
    '''
    cur.execute(print_db)
    while (True):
        state = cur.fetchone()
        if not state: break
        print("distance: ", state[1])
    
    cur.close()

def delete_touch_db(value = None): # value: None of "ON" / "OFF"
    cur = db_sensors.cursor()
    if (value == None):
        delete_db = '''
            delete from touch
        '''
        cur.execute(delete_db)

    else:
        delete_db = '''
            delete from touch WHERE state = %s
        '''
        cur.execute(delete_db, (value, ))
        
    db_sensors.commit()
    cur.close()