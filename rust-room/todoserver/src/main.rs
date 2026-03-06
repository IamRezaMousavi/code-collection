/**
 * @Author: @iamrezamousavi
 * @Date:   2023-03-24 02:17:10
 * @Last Modified by:   @iamrezamousavi
 * @Last Modified time: 2023-03-26 21:23:50
 */
use structopt::StructOpt;
use todoserver::server::TodoServer;

/// A minimul RESTful api
#[derive(StructOpt, Debug)]
#[structopt(name = "todoserver")]
struct Opt {
    /// Set host
    #[structopt(short, long, default_value = "127.0.0.1")]
    host: String,

    /// Set port
    #[structopt(short, long, default_value = "8080")]
    port: u16,
}

fn main() {
    let opt = Opt::from_args();
    let server = TodoServer::new(opt.host, opt.port);
    server.run().unwrap();
}
