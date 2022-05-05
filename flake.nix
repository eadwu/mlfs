{
  description = "Machine Learning From Scratch";

  # General Repositories
  inputs.nixpkgs = { type = "github"; owner = "NixOS"; repo = "nixpkgs"; ref = "nixos-21.05"; };
  inputs.flake-compat = { type = "github"; owner = "edolstra"; repo = "flake-compat"; flake = false; };

  # Reproducible Python Environments
  inputs.mach-nix = { type = "github"; owner = "DavHau"; repo = "mach-nix"; flake = false; };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      supportedSystems = [ "x86_64-linux" ];
      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

      config = { allowUnfree = true; };
      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit config system; overlays = [ self.overlay ]; });
    in
    {

      overlay = final: prev: {};

      devShell = forAllSystems (system:
        let
          pkgs = nixpkgsFor.${system};
          mach-nix = import inputs.mach-nix {
            inherit pkgs;
            python = "python39";

            # Latest dependency resolution chain as of `Jun 22 20:09:57 UTC 2021`
            pypiDataRev = "4ab020b5dab8fd927f275b257581cd1248e137bc";
            pypiDataSha256 = "1hjhsh283klw540gfp79r40xzd2xc9bp705r8cwx6v48pkgq67y3";
          };

          env = mach-nix.mkPython
            rec {
              requirements = ''
                numpy
                pandas
                protobuf
                matplotlib
                scikit-learn

                seaborn

                # PyTorch
                torch
                torchvision
                torchaudio

                # Jupyter
                jupyterlab
                notebook
                voila
              '';

              providers = {
                _default = "wheel,sdist,nixpkgs";
              };

              _.torch.src = pkgs.fetchurl {
                name = "torch-1.9.0+cu111-cp39-cp39-linux_x86_64.whl";
                url = "https://download.pytorch.org/whl/cu111/torch-1.9.0%2Bcu111-cp39-cp39-linux_x86_64.whl";
                sha256 = "VCLRkELiF8KqlAMLFrP+TaW+m6jupG5+WdQKEQlVli0=";
              };

              _.torchvision.src = pkgs.fetchurl {
                name = "torchvision-0.10.0+cu111-cp39-cp39-linux_x86_64.whl";
                url = "https://download.pytorch.org/whl/cu111/torchvision-0.10.0%2Bcu111-cp39-cp39-linux_x86_64.whl";
                sha256 = "AOfhnHThVdJx5qxj2LTj+T9dPMFxQoxP3duxIm1y7KE=";
              };

              _.torchaudio.src = pkgs.fetchurl {
                url = "https://download.pytorch.org/whl/torchaudio-0.9.0-cp39-cp39-linux_x86_64.whl";
                sha256 = "718LImRqlPlYaQAbQKuUBGixrjmdD/07xz1cQzQqATo=";
              };
            };
        in
        pkgs.mkShell {
          buildInputs = [ env ];

          # Direnv (Lorri) Support
          PYTHON_ENV = env.out;
        });

    };
}
