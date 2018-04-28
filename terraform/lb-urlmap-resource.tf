resource "google_compute_url_map" "main-urlmap" {
  name        = "main-urlmap"
  description = "Main url map"

  default_service = "${google_compute_backend_service.frontend-backendservice.self_link}"

  host_rule {
    hosts = ["djchangular.tk"]
    path_matcher = "frontend"
  }

  host_rule {
    hosts = ["api.djchangular.tk"]
    path_matcher = "backend"
  }

  path_matcher {
    default_service = "${google_compute_backend_service.backend-backendservice.self_link}"
    name = "backend"
  }

  path_matcher {
    default_service = "${google_compute_backend_service.frontend-backendservice.self_link}"
    name = "frontend"
  }
}