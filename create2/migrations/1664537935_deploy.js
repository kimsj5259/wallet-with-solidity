const DeterministicDeployFactory = artifacts.require("DeterministicDeployFactory");

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(DeterministicDeployFactory, "create2wallet!");
};
