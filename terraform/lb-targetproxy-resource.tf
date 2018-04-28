resource "google_compute_target_http_proxy" "main-targetproxy" {
  name        = "main-targetproxy"
  description = "Proxy to route traffic to the application"
  url_map     = "${google_compute_url_map.main-urlmap.self_link}"
}
