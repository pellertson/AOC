use fmt;
use fs;
use io;
use os;

export fn main() void = {
	const fn = "input.txt";
	const file = match(os::open(fn)) {
	case let file: io::file =>
		yield file;
	case let err: fs::error =>
		fmt::fatalf("Error opening {}: {}", fn, fs::strerror(err));
	};
};
