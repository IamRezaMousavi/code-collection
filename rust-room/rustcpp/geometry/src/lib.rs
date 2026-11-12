use std::ffi::CStr;
use std::os::raw::{c_char, c_int};

#[repr(C)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

#[unsafe(no_mangle)]
pub extern "C" fn point_new(x: i32, y: i32) -> Point {
    Point { x, y }
}

#[unsafe(no_mangle)]
pub extern "C" fn point_distance(a: Point, b: Point) -> f64 {
    let dx = (a.x - b.x) as f64;
    let dy = (a.y - b.y) as f64;

    (dx * dx + dy * dy).sqrt()
}

#[unsafe(no_mangle)]
pub extern "C" fn add_numbers(a: c_int, b: c_int) -> c_int {
    a + b
}

#[unsafe(no_mangle)]
pub extern "C" fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[unsafe(no_mangle)]
pub extern "C" fn greet(name: *const c_char) {
    if name.is_null() {
        return;
    }
    unsafe {
        if let Ok(s) = CStr::from_ptr(name).to_str() {
            println!("Hello from Rust: {}", s);
        }
    }
}

