class Detector:

    def __init__(self, temp, hum, pinbuzz):
        self.temp = temp 
        self.hum = hum
        self.pinbuzz = pinbuzz
    
    def calculate(self):
        
        if self.temp < 26:
            if self.hum < 55:
                return {"Temperature": "RENDAH", "Humidity": "RENDAH", "status_pompa": "ON"}
            elif self.hum >= 55 and self.hum <= 60:
                return {"Temperatur": "RENDAH", "Humudity" : "OPTIMAL", "status_pompa": "OFF"}
            elif self.hum > 60:
                return {"Temperature": "RENDAH", "Humudity": "TINGGI", "status_pomppa": "OFF"}
        elif self.temp >= 26 and self.temp <= 36:
            if self.hum < 55:       
                return {"Temperature": "OPTIMAL", "Humudity": "RENDAH", "status_pompa": "ON"}
            elif self.hum >= 55 and self.hum <= 60:
                return {"Temperature": "OPTIMAL", "Humudity": "OPTIMAL", "status_pompa": "OFF"}
            elif self.hum > 60:
                return {"Temperature": "OPTIMAL", "Humudity": "TINGGI", "status_pompa": "OFF"}
        elif self.temp > 36:
            if self.hum < 55:
                return {"Temperature": "TINGGI", "Humudity": "RENDAH", "status_pompa": "ON"}
            elif self.hum >= 55 and self.hum <= 60:
                return {"Temperature": "TINGGI", "Humudity": "OPTIMAL", "status_pompa": "OFF"}
            elif self.hum > 60:
                 return {"Temperature": "TINGGI", "Humudity": "TINGGI", "status_pompa": "OFF"}

    def buzz(self):
        from machine import PWM
        import time
        status_pompa = self.calculate()

        if status_pompa['status_pompa'] == 'ON':
            buzzer = PWM(self.pinbuzz)
            buzzer.freq(1047)
            buzzer.duty(50)
            time.sleep(1)
            buzzer.duty(0)
            buzzer.deinit()
            
