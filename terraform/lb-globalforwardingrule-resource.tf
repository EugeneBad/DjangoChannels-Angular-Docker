resource "google_compute_global_forwarding_rule" "main-gfr" {
  name       = "main-gfr"
  target     = "${google_compute_target_http_proxy.main-targetproxy.self_link}"
  port_range = "80"
}