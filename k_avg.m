indata=importdata('C:\Users\aoded\OneDrive\Documents\MATLAB\k_avg.csv');
rtl_1M=indata.data(:,1)';
usrp_1M=indata.data(:,2)';

figure(7);
clf('reset');
hold on; box on;
set(gca, 'LineWidth', 2, 'FontSize',30);%, 'Position', [.1 .1 3 5]);%,'PlotBoxAspectRatio',[3 1.5 1]);%, 'FontWeight', 'bold');
title('Sample Drop ratio (k)')
xlabel('Sample Rate')
ylabel('CDF');

plot(rtl_1M, 'r-s', 'LineWidth', 6, 'MarkerSize', 12)
plot(usrp_1M, 'b-^', 'LineWidth', 6, 'MarkerSize', 12)
%plot(perc_err, line_type{3}, 'LineWidth', 6, 'MarkerSize', 8)
ylim([0 1]);

xticks([1 2 3 4 5 6]);
xticklabels({'1', '2', '4', '8', '12', '16'});
%xtickangle(20);

leg1=['RTL'];% s=',num2str(scale)];
leg2=['USRP'];% s=',num2str(scale)];
%leg3=['Percentage error']% s=',num2str(scale)];
legend(leg1,leg2,'Location','Best')
legend boxoff

filename = ['C:\Users\aoded\OneDrive\Documents\MATLAB\1.eps'];
saveas(gca,filename,'epsc');
hold off;