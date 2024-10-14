%--------------------------------------------------------------------------
% Plot symbol's recordings from Panda Co-Manipulation Dataset
%
% Written by Giovanni Braglia, 2024
% University of Modena and Reggio Emilia
% 
% tested on MATLAB R2022a
%--------------------------------------------------------------------------

clear; clc; close all;

load("Panda_CoManipulation_Data/4/symbol_data.mat");
Ts = 0.001; % Sampling time of recordings

figure;  
for i=1:6
    L = length(symbol_data(i).pos);
    T = Ts*L; % Recording Duration
    t = linspace( 0, T, L );
    label = [ 'Rec', num2str(i) ];
    % Plot 2D symbol
    subplot(2,2,[1,3]); hold on;
    plot( symbol_data(i).pos(1,:), symbol_data(i).pos(2,:), LineWidth=2, DisplayName=label );
    % Plot x velocity
    subplot(2,2,2); hold on;
    plot( t, symbol_data(i).vel(1,:), LineWidth=2 );
    % Plot y velocity
    subplot(2,2,4); hold on;
    plot( t, symbol_data(i).vel(2,:), LineWidth=2 );
end

subplot(2,2,[1,3]);
%------------------ 
legend('Location','best'); box on; grid on;
xlim([-0.6,-0.35]);
ylim([-0.45,-0.15]);
xlabel( '$x$[m]','FontSize',14,'Interpreter','latex');
ylabel( '$y$[m]','FontSize',14,'Interpreter','latex');

subplot(2,2,2);
%------------------
box on; grid on;
xlabel( '$t$[s]','FontSize',14,'Interpreter','latex');
ylabel( '$\dot{x}$[m]','FontSize',14,'Interpreter','latex');

subplot(2,2,4);
%------------------
box on; grid on;
xlabel( '$t$[s]','FontSize',14,'Interpreter','latex');
ylabel( '$\dot{y}$[m]','FontSize',14,'Interpreter','latex');


