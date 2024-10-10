import MySQLdb

# mariaDB에 연결
db_sensors = MySQLdb.connect("localhost", "pwh1219", "1219", "week_5")

# aircon
# aircon의 상태를 input으로 받아 db에 저장하는 함수
def insert_aircon_info(aircon):
    # mariaDB에서 조작하기 위한 cursor 설정
    cur = db_sensors.cursor()
    if (aircon == 1):
        state = "ON"
    else:
        state = "OFF"
    insert_db = '''
        insert into aircon (state) values (%s)
    '''

    #aircon의 상태를 tuple 형태로 넣어줌
    cur.execute(insert_db, (state, ))
    # 변경상태 저장
    db_sensors.commit()
    # 사용한 cursor를 닫아줌
    cur.close()

#  DB에 저장되어있는 aircon의 상태를 출력하는 함수
#  함수의 매개변수로 아무것도 입력하지 않으면 DB의 모든 정보 출력
#  매개변수를 입력하면 가장 마지막으로 DB에 저장된 aircon의 상태, 시간 출력
def print_aircon_db(last = None): 
    cur = db_sensors.cursor()

    if (last == None):
        # DB의 모든 정보 출력
        print_db = '''
            select * from aircon
        '''
        cur.execute(print_db)
        while (True):
            # DB에서 한 줄씩 읽어옴
            temp = cur.fetchone()
            if not temp: break
            # tuple 형태로 저장되므로 aircon 상태, 저장된 시간을 순차로 출력
            print("aircon state: {}, time: {}".format(temp[0], temp[1]))
    # latest 정보 출력
    else:
        # DB의 값 중 가장 최신 값 한 개만 가져옴
        print_db = '''
            select state, dt FROM aircon
            ORDER BY dt DESC
            LIMIT 1
        '''
        cur.execute(print_db)
        # DB에서 한 줄씩 읽어옴
        temp = cur.fetchone()
        print("aircon state: {}, time: {}".format(temp[0], temp[1]))
    cur.close()

# DB에 저장된 정보를 지우는 함수
# 매개변수를 입력하지 않으면 DB의 모든 정보를 지움
# 매개변수를 입력하면 latest 값만 지움
def delete_aircon_db(value = None):
    cur = db_sensors.cursor()
    if (value == None):
        # DB에 저장된 모든 정보를 지움
        delete_db = '''
            delete from aircon
        '''
        cur.execute(delete_db)
    # DB의 latest 값만 지움
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
# 온습도센서에서 받은 온도 값을 받아 DB에 저장하는 함수
def insert_temperature_info(temp):
    # DB를 조작하기 위한 커서
    cur = db_sensors.cursor()
    insert_db = '''
        insert into temperature (temp) values (%s)
    '''
    # tuple 형태로 저장
    cur.execute(insert_db, (temp, ))
    # 변경 내용 저장
    db_sensors.commit()
    cur.close()

# 온도 DB의 모든 정보를 출력하는 함수
def print_temperature_db():
    cur = db_sensors.cursor()
    print_db = '''
        select * from temperature
    '''
    cur.execute(print_db)
    while (True):
        # DB의 정보를 한 줄씩 가져옴
        temp = cur.fetchone()
        if not temp: break
        # table의 column 순서가 id, temperature 순서이므로 temp[1]로 온도를 출력
        print("temperature: ", temp[1])
    
    cur.close()

# DB에 저장된 정보를 지우는 함수
# 매개변수를 입력하지 않으면 temperature table에 저장된 모든 정보를 지움
# 매개변수를 입력하면 특정 온도값만 지움
def delete_temperature_db(value = None):
    cur = db_sensors.cursor()
    # temperature의 모든 정보를 지움
    if (value == None):
        delete_db = '''
            delete from temperature
        '''
        cur.execute(delete_db)
    # 입력받은 온도 값만 table에서 지움
    else:
        delete_db = '''
            delete from temperature WHERE temp = %s
        '''
        cur.execute(delete_db, (value, ))
    # 변경정보 저장
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