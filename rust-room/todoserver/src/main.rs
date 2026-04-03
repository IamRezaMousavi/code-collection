/**
 * @Author: @iamrezamousavi
 * @Date:   2023-03-24 02:17:10
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2026-04-03 12:14:28
 */

use clap::Parser;
use todoserver::server::TodoServer;

/// A minimal RESTful api
#[derive(Parser, Debug)]
#[command(version, about)]
struct Args {
    /// Set host ip
    #[arg(short, long, default_value = "127.0.0.1")]
    ip: String,

    /// Set port
    #[arg(short, long, default_value = "8080")]
    port: u16,
}

fn main() {
    let args = Args::parse();
    let server = TodoServer::new(args.ip, args.port);
    server.run().unwrap();
}
