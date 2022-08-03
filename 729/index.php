<?php

class MyCalendar {
    public $bookings;
    
    /**
     */
    function __construct() {
        $this->bookings = [];
    }
  
    /**
     * @param Integer $start
     * @param Integer $end
     * @return Boolean
     */
    function book($start, $end) {
        
        
        // If none of the values are provided
        if(($start == null && $end == null ) || ($start === $end)) {
            return null;
        }
        
        // Check if start date is already booked
        if(count($this->bookings) > 0) {
            foreach($this->bookings as $booking) {
                if($start < $booking[1] && $end > $booking[0]) {
                    return false;
                } 
            }
            
            $this->bookings[] = [$start, $end]; 
            return true;

        } else {
            $this->bookings[] = [$start, $end];  
            return true;
        }
    }
}

$obj = new MyCalendar();
$ret = $obj->book(10, 20);
$ret_2 = $obj->book(5, 10);
$ret_3 = $obj->book(0, 5);
